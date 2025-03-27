#PremSub

import os

from dotenv import load_dotenv

load_dotenv(".env")



BOT_TOKEN = os.environ.get("BOT_TOKEN", "7664621137:AAGKbBpdOBfApMxF4lCtgQHEjUpJhucZGls")
API_ID = int(os.environ.get("API_ID", "8986091"))
API_HASH = os.environ.get("API_HASH", "c568be6936fb9df2a9ac17cce099e748")
MONGO_URL = os.environ.get("MONGO_URL", "mongodb+srv://zacnmusic:zacnmusic@cluster0.jhgvg.mongodb.net/?retryWrites=true&w=majority&appName=ZACNHERE")
ADMINS = [int(x) for x in (os.environ.get("ADMINS", "1361379181").split())]
MEMBER = [int(x) for x in (os.environ.get("MEMBER", "").split())]
LOG_GRP = int(os.environ.get("LOG_GRP", "-1002166782827"))
BOT_ID = int(os.environ.get("BOT_ID", "7664621137"))
NamaData = os.environ.get("NamaData", "ZacnFsub")

KITA = [int(x) for x in (os.environ.get("KITA", "1361379181 1361379181").split())]
