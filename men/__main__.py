import asyncio
import re
from io import BytesIO

import requests
from config import *
from pyrogram import *
from men import app, list_admins, member_permissions, extract_user
from pler import kntl
from db import *
from pytz import timezone
import datetime
from men.helpers.tools import *
from men.helpers.database import *
from dateutil.relativedelta import relativedelta





async def init():
    await app.start()
    await premtool()
    await idle()
    await app.stop()

@app.on_message(filters.command("protect", PREFIX) & ~filters.private)
@prouser
# @language
async def anti_anti(_, m):
    if len(m.command) != 2:
        return await m.reply_text("Usage: /atigikes [on|off]")
    status = m.text.split(None, 1)[1].strip()
    status = status.lower()
    chat_id = m.chat.id
    if status == "on":
        if await is_antigcast_on(chat_id):
            await m.reply_text("Anti-Gcast Active Bos")
        else:
            await antigcast_on(chat_id)
            await m.reply_text(
                "ANTIGIKES telah aktif, Saya akan memulai menghapus pesan busuk!."
            )
    elif status == "off":
        if not await is_antigcast_on(chat_id):
            await m.reply_text("Protec Anti-Gcast sudah MATI.")
        else:
            await antigcast_off(chat_id)
            await m.reply_text(
                "ANTIGCAST sudah mati, Saya tidak akan menghapus pesan!"
            )
    else:
        await m.reply_text("Unknown Suffix, Use /protec [on|off]")


async def isGcast(filter, c, update):
    bl = "҈💋༙༙༙༙༙༙I+𖤐O͛͟O͛͟𖤐𖤐˚༙༙༙༙𓏲࣪爱⪨✮⋆⌕🜲ᕕຊᕗ⊃‿★±♪♫⊶𒀭⨮❥⨶⨁⨷❍❏≋‌❥€¥¢£¢a̴b̴c̴d̴e̴f̴g̴h̴i̴j̴k̴l̴m̴n̴o̴p̴q̴r̴s̴t̴u̴v̴w̴x̴y̴z̴A̴B̴C̴D̴E̴F̴G̴H̴I̴J̴K̴L̴M̴N̴O̴P̴Q̴R̴S̴T̴U̴V̴W̴X̴Y̴Z̴a͟b͟c͟d͟e͟f͟g͟h͟i͟j͟k͟l͟m͟n͟o͟p͟q͟r͟s͟t͟u͟v͟w͟x͟y͟z͟A͟B͟C͟D͟E͟F͟G͟H͟I͟J͟K͟L͟M͟N͟O͟P͟Q͟R͟S͟T͟U͟V͟W͟X͟Y͟Z͟҈a҈҈b҈҈c҈҈d҈҈e҈҈f҈҈g҈҈h҈҈i҈҈j҈҈k҈҈l҈҈m҈҈n҈҈o҈҈p҈҈q҈҈r҈҈s҈҈t҈҈u҈҈v҈҈w҈҈x҈҈y҈҈z҈҈A҈҈B҈҈C҈҈D҈҈E҈҈F҈҈G҈҈H҈҈I҈҈J҈҈K҈҈L҈҈M҈҈N҈҈O҈҈P҈҈Q҈҈R҈҈S҈҈T҈҈U҈҈V҈҈W҈҈X҈҈Y҈҈Z҈҉ȃ̮b̮̑c̮̑d̮̑ȇ̮f̮̑g̮̑ḫ̑ȋ̮j̮̑k̮̑l̮̑m̮̑n̮̑ȏ̮p̮̑q̮̑ȓ̮s̮̑t̮̑ȗ̮v̮̑w̮̑x̮̑y̮̑z̮̑Ȃ̮B̮̑C̮̑D̮̑Ȇ̮F̮̑G̮̑Ḫ̑Ȋ̮J̮̑K̮̑L̮̑M̮̑N̮̑Ȏ̮P̮̑Q̮̑Ȓ̮S̮̑T̮̑Ȗ̮V̮̑W̮̑X̮̑Y̮̑Z̮̑a̶b̶c̶d̶e̶f̶g̶h̶i̶j̶k̶l̶m̶n̶o̶p̶q̶r̶s̶t̶u̶v̶w̶x̶y̶z̶A̶B̶C̶D̶E̶F̶G̶H̶I̶J̶K̶L̶M̶N̶O̶P̶Q̶R̶S̶T̶U̶V̶W̶X̶Y̶Z̶a҉҉b҉҉c҉҉d҉҉e҉҉f҉҉g҉҉h҉҉i҉҉j҉҉k҉҉l҉҉m҉҉n҉҉o҉҉p҉҉q҉҉r҉҉s҉҉t҉҉u҉҉v҉҉w҉҉x҉҉y҉҉z҉҉A҉҉B҉҉C҉҉D҉҉E҉҉F҉҉G҉҉H҉҉I҉҉J҉҉K҉҉L҉҉M҉҉N҉҉O҉҉P҉҉Q҉҉R҉҉S҉҉T҉҉U҉҉V҉҉W҉҉X҉҉Y҉҉Z҉₳฿ȻƉɆŦǤĦłJ₭Ⱡ₥₦Ø₱QⱤ₴₮ɄV₩ӾɎƵ₳฿ȻƉɆŦǤĦłJ₭Ⱡ₥₦Ø₱QⱤ₴₮ɄV₩ӾɎƵ⍺ɓƈɗⱸʆɠɦίʝƙȴɱȵơƥʠɽ᥉ȶ᭘꣗᭙᥊λßƈđëƒǥħïjƙłмŋøρqЯƨŧųvшх¥ƺΛßƇÐËҒƓĦÏJҠŁ₥ŊØPǪЯƧŧųVЩЖΫZƴʑ⍺ɓƈɗⱸʆɠɦίʝƙȴɱȵơƥʠɽ᥉ȶ᭘꣗᭙᥊ƴʑⲇⲃⲥ𝖽ⲉfⳋⲏⳕⳗқⳑϻⲛⲟⳏⳝⲅ⳽τυⳳⲱⲭⲩⲹⲇⲃⲥ𝖽ⲉfⳋⲏⳕⳗқⳑϻⲛⲟⳏⳝⲅ⳽τυⳳⲱⲭⲩⲹ𖤬ꔪꛕ𖤀𖤟ꘘꚽꛅꛈꚠ𖤰ꚳ𖢑ꛘ𖣠ㄗꚩ𖦪ꕷ𖢧ꚶꚴꛃ𖤗ꚲꛉ𖤬ꔪꛕ𖤀𖤟ꘘꚽꛅꛈꚠ𖤰ꚳ𖢑ꛘ𖣠ㄗꚩ𖦪ꕷ𖢧ꚶꚴꛃ𖤗ꚲꛉɑხɕᑯɛƒɡҺıʝꮶꝇ꧑ꞃᴏթɋɾ᥉ꞇᤙ᥎ꝫ᥊ƴᤁɑხɕᑯɛƒɡҺıʝꮶꝇ꧑ꞃᴏթɋɾ᥉ꞇᤙ᥎ꝫ᥊ƴᤁꋬꃳꉔ꒯ꏂꊰꍌꁝ꒐꒻ꀘ꒒ꂵꋊꄲꉣꆰꋪꇙ꓄꒤꒦ꅐꉧꌦꁴꋬꃳꉔ꒯ꏂꊰꍌꁝ꒐꒻ꀘ꒒ꂵꋊꄲꉣꆰꋪꇙ꓄꒤꒦ꅐꉧꌦꁴᎯᏰᏨᎠᎬᎰᎶᎻᎨᏠᏦᏝᎷᏁᎾᏢᏅᏒᏕᏖᏬᏉᏯᎲᎽᏃᎯᏰᏨᎠᎬᎰᎶᎻᎨᏠᏦᏝᎷᏁᎾᏢᏅᏒᏕᏖᏬᏉᏯᎲᎽᏃ𝑎𝑏𝑐𝑑𝑒𝑓𝑔𝒉𝑖𝑗𝑘𝑙𝑚𝑛𝑜𝑝𝑞𝑟𝑠𝑡𝑢𝑣𝑤𝑥𝑦𝑧𝐴𝐵𝐶𝐷𝐸𝐹𝐺𝐻𝐼𝐽𝐾𝐿𝑀𝑁𝑂𝑃𝑄𝑅𝑆𝑇𝑈𝑉𝑊𝑋𝑌𝑍𝘢𝘣𝘤𝘥𝘦𝘧𝘨𝘩𝘪𝘫𝘬𝘭𝘮𝘯𝘰𝘱𝘲𝘳𝘴𝘵𝘶𝘷𝘸𝘹𝘺𝘻𝘈𝘉𝘊𝘋𝘌𝘍𝘎𝘏𝘐𝘑𝘒𝘓𝘔𝘕𝘖𝘗𝘘𝘙𝘚𝘛𝘜𝘝𝘞𝘟𝘠𝘡𝕒𝕓𝕔𝕕𝕖𝕗𝕘𝕙𝕚𝕛𝕜𝕝𝕞𝕟𝕠𝕡𝕢𝕣𝕤𝕥𝕦𝕧𝕨𝕩𝕪𝕫𝔸𝔹ℂ𝔻𝔼𝔽𝔾ℍ𝕀𝕁𝕂𝕃𝕄ℕ𝕆ℙℚℝ𝕊𝕋𝕌𝕍𝕎𝕏𝕐ℤ×‌ⓐⓑⓒⓓⓔⓕⓖⓗⓘⓙⓚⓛⓜⓝⓞⓟⓠⓡⓢⓣⓤⓥⓦⓧⓨⓩⒶⒷⒸⒹⒺⒻⒼⒽⒾⒿⓀⓁⓂ️ⓃⓄⓅⓆⓇⓈⓉⓊⓋⓌⓍⓎⓏ🅐🅑🅒🅓🅔🅕🅖🅗🅘🅙🅚🅛🅜🅝🅞🅟🅠🅡🅢🅣🅤🅥🅦🅧🅨🅩🅐🅑🅒🅓🅔🅕🅖🅗🅘🅙🅚🅛🅜🅝🅞🅟🅠🅡🅢🅣🅤🅥🅦🅧🅨🅩🄰🄱🄲🄳🄴🄵🄶🄷🄸🄹🄺🄻🄼🄽🄾🄿🅀🅁🅂🅃🅄🅅🅆🅇🅈🅉🄰🄱🄲🄳🄴🄵🄶🄷🄸🄹🄺🄻🄼🄽🄾🄿🅀🅁🅂🅃🅄🅅🅆🅇🅈🅉🅰️🅱️🅲🅳🅴🅵🅶🅷🅸🅹🅺🅻🅼🅽🅾️🅿️🆀🆁🆂🆃🆄🆅🆆🆇🆈🆉🅰️🅱️🅲🅳🅴🅵🅶🅷🅸🅹🅺🅻🅼🅽🅾️🅿️🆀🆁🆂🆃🆄🆅🆆🆇🆈🆉🇦 🇧 🇨 🇩 🇪 🇫 🇬 🇭 🇮 🇯 🇰 🇱 🇲 🇳 🇴 🇵 🇶 🇷 🇸 🇹 🇺 🇻 🇼 🇽 🇾 🇿 🇦 🇧 🇨 🇩 🇪 🇫 🇬 🇭 🇮 🇯 🇰 🇱 🇲 🇳 🇴 🇵 🇶 🇷 🇸 🇹 🇺 🇻 🇼 🇽 🇾 🇿 ᴀʙᴄᴅᴇғɢʜɪᴊᴋʟᴍɴᴏᴘϙʀᴛᴜᴠᴡʏᴢᴀʙᴄᴅᴇғɢʜɪᴊᴋʟᴍɴᴏᴘϙʀᴛᴜᴠᴡʏᴢᵃᵇᶜᵈᵉᶠᵍʰⁱʲᵏˡᵐⁿᵒᵖᵠʳˢᵗᵘᵛʷˣʸᶻᵃᵇᶜᵈᵉᶠᵍʰⁱʲᵏˡᵐⁿᵒᵖᵠʳˢᵗᵘᵛʷˣʸᶻᵃᵇᶜᵈᵉᶠᵍʰⁱʲᵏˡᵐⁿᵒᵖᵠʳˢᵗᵘᵛʷˣʸᶻᴀʙᴄᴅᴇғɢʜɪᴊᴋʟᴍɴᴏᴘϙʀᴛᴜᴠᴡʏᴢᗩᗷᑕᗞᗴᖴᏀᕼᏆᒍᏦしᗰᑎᝪᑭᑫᖇᔑᎢᑌᐯᗯ᙭ᎩᏃᗩᗷᑕᗞᗴᖴᏀᕼᏆᒍᏦしᗰᑎᝪᑭᑫᖇᔑᎢᑌᐯᗯ᙭ᎩᏃᎪᏴᏟᎠᎬҒᏀᎻᏆᎫᏦᏞᎷΝϴᏢϘᎡՏͲႮᏙᏔХᎽᏃᎪᏴᏟᎠᎬҒᏀᎻᏆᎫᏦᏞᎷΝϴᏢϘᎡՏͲႮᏙᏔХᎽᏃａｂｃｄｅｆｇｈｉｊｋｌｍｎｏｐｑｒｓｔｕｖｗｘｙｚＡＢＣＤＥＦＧＨＩＪＫＬＭＮＯＰＱＲＳＴＵＶＷＸＹＺ𝗮𝗯𝗰𝗱𝗲𝗳𝗴𝗵𝗶𝗷𝗸𝗹𝗺𝗻𝗼𝗽𝗾𝗿𝘀𝘁𝘂𝘃𝘄𝘅𝘆𝘇𝗔𝗕𝗖𝗗𝗘𝗙𝗚𝗛𝗜𝗝𝗞𝗟𝗠𝗡𝗢𝗣𝗤𝗥𝗦𝗧𝗨𝗩𝗪𝗫𝗬𝗭𝙖𝙗𝙘𝙙𝙚𝙛𝙜𝙝𝙞𝙟𝙠𝙡𝙢𝙣𝙤𝙥𝙦𝙧𝙨𝙩𝙪𝙫𝙬𝙭𝙮𝙯𝘼𝘽𝘾𝘿𝙀𝙁𝙂𝙃𝙄𝙅𝙆𝙇𝙈𝙉𝙊𝙋𝙌𝙍𝙎𝙏𝙐𝙑𝙒𝙓𝙔𝙕𝚊𝚋𝚌𝚍𝚎𝚏𝚐𝚑𝚒𝚓𝚔𝚕𝚖𝚗𝚘𝚙𝚚𝚛𝚜𝚝𝚞𝚟𝚠𝚡𝚢𝚣𝙰𝙱𝙲𝙳𝙴𝙵𝙶𝙷𝙸𝙹𝙺𝙻𝙼𝙽𝙾𝙿𝚀𝚁𝚂𝚃𝚄𝚅𝚆𝚇𝚈𝚉𝐚𝐛𝐜𝐝𝐞𝐟𝐠𝐡𝐢𝐣𝐤𝐥𝐦𝐧𝐨𝐩𝐪𝐫𝐬𝐭𝐮𝐯𝐰𝐱𝐲𝐳𝐀𝐁𝐂𝐃𝐄𝐅𝐆𝐇𝐈𝐉𝐊𝐋𝐌𝐍𝐎𝐏𝐐𝐑𝐒𝐓𝐔𝐕𝐖𝐗𝐘𝐙𝒂𝒃𝒄𝒅𝒆𝒇𝒈𝒉𝒊𝒋𝒌𝒍𝒎𝒏𝒐𝒑𝒒𝒓𝒔𝒕𝒖𝒗𝒘𝒙𝒚𝒛𝑨𝑩𝑪𝑫𝑬𝑭𝑮𝑯𝑰𝑱𝑲𝑳𝑴𝑵𝑶𝑷𝑸𝑹𝑺𝑻𝑼𝑽𝑾𝑿𝒀𝒁"
    awoos = update.text
    user = update.from_user.id
    x = awoos.lower()
    with open('bl.txt', 'r') as file:
        blc = [w.lower().strip() for w in file.readlines()]
        for chara in bl:
            blc.append(chara)
    bluser = await is_bisu_user(user)
    for chara in blc:
        if chara in x:
            return True
    if bluser:
        return True
    if x in await bl_bang():
        return True

    return False


Gcast = filters.create(isGcast)


@app.on_message(filters.text & filters.group & Gcast, group=-1)
@anti_gcast
async def deletermessag(app, m):
    chat_id = m.chat.id
    user = m.from_user
    if chat_id not in await cek_pro():
        return
    if not user:
        return
    elif user.id in await list_admins(chat_id):
        return

    try:
        await app.delete_messages(chat_id, message_ids=m.id)
    except FloodWait as e:
        await asyncio.sleep(e.value)
        await app.delete_messages(chat_id, message_ids=m.id)
    except MessageDeleteForbidden:
        return

@app.on_message(filters.command(["piw"], PREFIX) & ~filters.private & filters.user(OWNER_ID))
async def banFunc(_, m):
    ijin = await member_permissions(m.chat.id, m.from_user.id)
    xx = "can_restrict_members"
    if xx not in ijin:
        return
    user_id = await extract_user(m)
    if not user_id:
        return
    if user_id == app.me.id:
        return
    if user_id in OWNER_ID:
        return
    if user_id in (await list_admins(m.chat.id)):
        return
    dicekah = await is_bisu_user(user_id)
    if dicekah:
        return await m.reply_text("Binatang Liar Ini Sudah Terblacklist Bos.")
    try:
        mention = (await app.get_users(user_id)).mention
    except IndexError:
        mention = (
            m.reply_to_m.sender_chat.title
            if m.reply_to_message
            else "Anon"
        )
    await add_bisu_user(user_id)
    return await m.reply(f"User : {mention} Binatang Liar Ini Sudah Terblacklist Bos.")

@app.on_message(filters.command(["lepas"], PREFIX) & ~filters.private & filters.user(OWNER_ID))
async def banFunc(_, m):
    ijin = await member_permissions(m.chat.id, m.from_user.id)
    xx = "can_restrict_members"
    if xx not in ijin:
        return
    user_id = await extract_user(m)
    if not user_id:
        return
    dicekah = await is_bisu_user(user_id)
    if not dicekah:
        return await m.reply_text("Binatang Liar Terlepas Dari Blacklist Bos.")
    try:
        mention = (await app.get_users(user_id)).mention
    except IndexError:
        mention = (
            m.reply_to_m.sender_chat.title
            if m.reply_to_message
            else "Anon"
        )
    await remove_bisu_user(user_id)
    return await m.reply(f"User : {mention} sudah di masukan ke daftar putih.")

@app.on_message(filters.command(["pro"], PREFIX))
@prouser
async def diproin(c, m):
    chat_id = (
        m.chat.id if m.chat.id else int(m.text.strip().split()[1])
    )
    if chat_id in await cek_pro():
        return
    diprokan = await add_pro(chat_id)
    if diprokan:
        return
    else:
        await m.reply_text("Added to Anti-Gcast.")

@app.on_message(filters.command(["prem"], PREFIX))
@prouser
async def dipremin(c, m):
    chat_id = (
        m.chat.id if m.chat.id else int(m.text.strip().split()[1])
    )
    if chat_id in await get_prem():
        return
    dipremin = await add_prem(chat_id)
    if dipremin:
        return
    else:
        await m.reply_text("PREM AKTIF**\nGroup : `{chat_id}`\nExp | `30 Hari..`**.")





@app.on_message(filters.command("listpro", PREFIX))
@prouser
async def KONTOL(c, m):
    text = ""
    for count, chat_id in enumerate(await cek_pro(), 1):
        try:
            title = (await app.get_chat(chat_id)).title
        except Exception:
            title = "Private"
        text += "<b>• {count}. {title} [<code>{chat_id}</code>]</b>\n".format(count, title, chat_id)
    if text == "":
        return
    await m.reply_text(text)


@app.on_message(filters.command(["unpro"], PREFIX))
@prouser
async def diproin(c, m):
    chat_id = (
        m.chat.id if m.chat.id else int(m.text.strip().split()[1])
    )
    if chat_id not in await cek_pro():
        return
    diprokan = await remove_pro(chat_id)
    if diprokan:
        await m.reply_text("Berhasil di hapus dari daftar antigikes")
    else:
        return


if __name__ == "__main__":
    loop = asyncio.get_event_loop_policy().get_event_loop()
    loop.run_until_complete(init())
    kntl.run_until_disconnected()
