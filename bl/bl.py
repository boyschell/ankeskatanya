import asyncio
import html
import re
from time import time
from datetime import datetime, timedelta
from pyrogram.enums import ParseMode
from pyrogram import filters
from pyrogram.types import ChatPermissions, Message

from ankeskatanya import app
from ankeskatanya.misc import SUDOERS
from ankeskatanya.utils.decorators.errors import capture_err
from ankeskatanya.utils.decorators.permissions import adminsOnly
from ankeskatanya.utils.decorators.admins1 import list_admins
from ankeskatanya.utils.database import (
    delete_blacklist_filter,
    get_blacklisted_words,
    save_blacklist_filter,
)
from ankeskatanya.utils.filter_group import blacklist_filters_group



@app.on_message(filters.command("bl") & ~filters.private)
@adminsOnly("can_restrict_members")
async def save_filters(_, message: Message):
    user = message.from_user
    admin_list = await list_admins(message.chat.id)
    if user.id not in admin_list:
        return
    chat_id = message.chat.id
    is_reply = True if message.reply_to_message else False
    if is_reply:
        words = message.reply_to_message.text if message.reply_to_message else message.text
    else:
        words = " ".join(message.command[1:])
    if not words:
        return await message.reply_text("balas atau masukan pesan")
    if len(words) > 1:
        text = words
        to_blacklist = list(
            {trigger.strip() for trigger in text.split("\n") if trigger.strip()},
        )
        for trigger in to_blacklist:
            await save_blacklist_filter(chat_id, trigger.lower())
           # await save_blacklist_filter(-1001955725516, trigger.lower())
           # await save_blacklist_filter(-1002041187558, trigger.lower())
           # await save_blacklist_filter(-1001953414079, trigger.lower())
           # await save_blacklist_filter(-1001817181967, trigger.lower())
           # await save_blacklist_filter(-1001722106344, trigger.lower())
        if is_reply:
            await message.reply_to_message.delete()
        if len(to_blacklist) == 1:
            add = await message.reply_text(
                f"Added <code>{html.escape(to_blacklist[0])}</code> to the blacklist filters!",
                parse_mode=ParseMode.HTML,
            )
        else:
            add = await message.reply_text(
                f"Added <code>{len(to_blacklist)}</code> triggers to the blacklist filters!",
                parse_mode=ParseMode.HTML,
            )
        await asyncio.sleep(1)
        await add.delete()
        await message.delete()
    else:
        await message.reply_text(
            "Usage:\n/bl [triggers] - The words/sentences you want to blacklist",
)

@app.on_message(filters.command("listbl") & ~filters.private)
@capture_err
async def get_filterss(_, message):
    data = await get_blacklisted_words(message.chat.id)
    if not data:
        await message.reply_text("**No blacklisted words in this chat.**")
    else:
        msg = f"List of blacklisted words in {message.chat.title} :\n"
        for word in data:
            msg += f"**-** `{word}`\n"
        await message.reply_text(msg)


@app.on_message(filters.command("delbl") & ~filters.private)
@adminsOnly("can_restrict_members")
async def del_filter(_, message):
    if len(message.command) < 2:
        return await message.reply_text("Gunakan:\n/delbl balas atau masukan pesan]")
    word = message.text.split(None, 1)[1].strip()
    if not word:
        return await message.reply_text("Gunakan:\n/delbl balas atau masukan pesan")
    chat_id = message.chat.id
    deleted = await delete_blacklist_filter(chat_id, word)
    if deleted:
        return await message.reply_text(f"**Whitelisted {word}.**")
    await message.reply_text("**No such blacklist filter.**")


@app.on_message(filters.text & ~filters.private, group=blacklist_filters_group)
@capture_err
async def blacklist_filters_re(_, message):
    text = message.text.lower().strip()
    if not text:
        return
    chat_id = message.chat.id
    user = message.from_user
    if not user:
        return
    if user.id in SUDOERS:
        return
    list_of_filters = await get_blacklisted_words(chat_id)
    for word in list_of_filters:
        pattern = r"( |^|[^\w])" + re.escape(word) + r"( |$|[^\w])"
        if re.search(pattern, text, flags=re.IGNORECASE):
            if user.id in await list_admins(chat_id):
                return
            try:
                await message.delete()
            except Exception as e:
                print(e, "error in blacklist filter")
                return
