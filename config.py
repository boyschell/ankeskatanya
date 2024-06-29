import os

from dotenv import load_dotenv

load_dotenv()


API_ID = int(os.getenv("API_ID", "29320516"))
API_HASH = os.getenv("API_HASH", "bcc68b59eb17c36b951965de3247a59d")
TOKEN = os.getenv("TOKEN", "7044533795:AAFjtB8t4-7fc7EbjmASQBxnjEiZGkcYe3A")
DB_NAME = os.getenv("DB_NAME", "pler")
MONGO = os.getenv("MONGO", "mongodb+srv://assistantchell:chell1234@cluster0.txscyxy.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")
GOKIL = ". ! ? / , - +"
PREFIX = GOKIL.split()
OWNER_ID = list(map(int, os.getenv("OWNER_ID", "5272203652").split()))
LOGGER_ID = int(getenv("LOGGER_ID", -1002063271971))
