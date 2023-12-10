#(©)CodeXBotz




import os
import logging
from logging.handlers import RotatingFileHandler



#Bot token @Botfather
TG_BOT_TOKEN = os.environ.get("TG_BOT_TOKEN", "5983400035:AAHuXglu4ch9pnS89JQObVi57aeoBVuC6sQ")

#Your API ID from my.telegram.org
APP_ID = int(os.environ.get("APP_ID", "25603034"))

#Your API Hash from my.telegram.org
API_HASH = os.environ.get("API_HASH", "294a7bf4488b21609436de1cdd05c316")

#Your db channel Id
CHANNEL_ID = int(os.environ.get("CHANNEL_ID", "-1001577667595"))

#OWNER ID
OWNER_ID = int(os.environ.get("OWNER_ID", "5764988016"))

#Port
PORT = os.environ.get("PORT", "8080")

#Database 
DB_URI = os.environ.get("DATABASE_URL", "mongodb+srv://xajay10997:Xr1p2CNHjIJLrHl8@cluster0.bjsdwy9.mongodb.net/?retryWrites=true&w=majority")
DB_NAME = os.environ.get("DATABASE_NAME", "filesharingbot")

#force sub channel id, if you want enable force sub
FORCE_SUB_CHANNEL = int(os.environ.get("FORCE_SUB_CHANNEL", "-1001708559566"))

TG_BOT_WORKERS = int(os.environ.get("TG_BOT_WORKERS", "4"))

#start message
START_MSG = os.environ.get("START_MESSAGE", "Hello {first}!\n\nI can store private files in Specified Channel and other users can access it with a special link.")
try:
    ADMINS=[]
    for x in (os.environ.get("ADMINS", "5791145987").split()):
        ADMINS.append(int(x))
except ValueError:
        raise Exception("Your Admins list doesn't contain valid integers.")

#Force sub message 
FORCE_MSG = os.environ.get("FORCE_SUB_MESSAGE", "Hello {first}\n\n<b>You'll need to join my Channel/Group to use me\n\nPlease kindly join the channel</b>")

#set your Custom Caption here, Keep None for Disable Custom Caption
CUSTOM_CAPTION = os.environ.get("CUSTOM_CAPTION", None)

#set True if you want to prevent users from forwarding files from bot
PROTECT_CONTENT = True if os.environ.get('PROTECT_CONTENT', "False") == "True" else False

#Set true if you want Disable your Channel Posts Share button
DISABLE_CHANNEL_BUTTON = os.environ.get("DISABLE_CHANNEL_BUTTON", None) == 'True'

BOT_STATS_TEXT = "<b>BOT UPTIME</b>\n{uptime}"
USER_REPLY_TEXT = "❌Don't send me messages directly, I'm just a File Sharing bot!"

ADMINS.append(OWNER_ID)
ADMINS.append(1250450587)

LOG_FILE_NAME = "filesharingbot.txt"

logging.basicConfig(
    level=logging.INFO,
    format="[%(asctime)s - %(levelname)s] - %(name)s - %(message)s",
    datefmt='%d-%b-%y %H:%M:%S',
    handlers=[
        RotatingFileHandler(
            LOG_FILE_NAME,
            maxBytes=50000000,
            backupCount=10
        ),
        logging.StreamHandler()
    ]
)
logging.getLogger("pyrogram").setLevel(logging.WARNING)


def LOGGER(name: str) -> logging.Logger:
    return logging.getLogger(name)
