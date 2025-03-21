#PremSub

import os

from dotenv import load_dotenv

load_dotenv(".env")



BOT_TOKEN = os.environ.get("BOT_TOKEN", "")
API_ID = int(os.environ.get("API_ID", "18932594"))
API_HASH = os.environ.get("API_HASH", "")
MONGO_URL = os.environ.get("MONGO_URL", "")
ADMINS = [int(x) for x in (os.environ.get("ADMINS", "1325957770").split())]
MEMBER = [int(x) for x in (os.environ.get("MEMBER", "1325957770").split())]
LOG_GRP = int(os.environ.get("LOG_GRP", "-1002173200214"))
BOT_ID = int(os.environ.get("BOT_ID", "7152159664"))
NamaData = os.environ.get("NamaData", "ZeebFsub")

KITA = [int(x) for x in (os.environ.get("KITA", "1325957770 1325957770").split())]
