from operator import add
import os
import logging


# import dotenv
# dotenv.load_dotenv()



from logging.handlers import RotatingFileHandler

#force user to join your backup channel leave 0 if you don't need.
FORCE_SUB_CHANNEL = int(os.environ.get("FORCE_SUB_CHANNEL", "-1002396393602"))
FORCE_SUB_CHANNEL2 = int(os.environ.get("FORCE_SUB_CHANNEL2", "-1002125606566"))

if FORCE_SUB_CHANNEL > FORCE_SUB_CHANNEL2:
    temp = FORCE_SUB_CHANNEL2 
    FORCE_SUB_CHANNEL2 = FORCE_SUB_CHANNEL
    FORCE_SUB_CHANNEL = temp


if FORCE_SUB_CHANNEL2 > FORCE_SUB_CHANNEL:
    temp = FORCE_SUB_CHANNEL 
    FORCE_SUB_CHANNEL = FORCE_SUB_CHANNEL2
    FORCE_SUB_CHANNEL2 = temp


#bot stats
BOT_STATS_TEXT = os.environ.get("BOTS_STATS_TEXT","<b>BOT UPTIME </b>\n{uptime}")
#send custom message when user interact with bot
USER_REPLY_TEXT = os.environ.get("USER_REPLY_TEXT", "Don't send me messages directly I'm only File Share bot! ")


#your bot token here from https://telegram.me/BotFather
TG_BOT_TOKEN = os.environ.get("TG_BOT_TOKEN", "7713796326:AAEDCPkMkXStmbzKq4OPG-UsN4AIavUPWv4") 
#your api id from https://my.telegram.org/apps
APP_ID = int(os.environ.get("APP_ID", "21484586"))
#your api hash from https://my.telegram.org/apps
API_HASH = os.environ.get("API_HASH", "d1d12be1da9b5a1cb8356c0bf0695a23")
#your channel_id from https://t.me/MissRose_bot by forwarding dummy message to rose and applying command `/id` in reply to that message
CHANNEL_ID = int(os.environ.get("CHANNEL_ID", "-1002298993427"))
#your id of telegram can be found by https://t.me/MissRose_bot with '/id' command
OWNER_ID = int(os.environ.get("OWNER_ID", "5915807321"))
#port set to default 8080
PORT = os.environ.get("PORT", "2222")
#your database url mongodb only You can use mongo atlas free cloud database
DB_URL = os.environ.get("DB_URL", "mongodb+srv://koyeb77user:rohit870@cluster0.wgdkp.mongodb.net/?retryWrites=true&w=majority")
#your database name
DB_NAME = os.environ.get("DB_NAME", "filestorabot")

#for creating telegram thread for bot to improve performance of the bot
TG_BOT_WORKERS = int(os.environ.get("TG_BOT_WORKERS", "4"))
#your start default command message.
START_MSG = os.environ.get("START_MESSAGE", "Hello {first}\n\nI can store private files in Specified Channel and other users can access it from special link. ")
#your telegram tag without @
OWNER_TAG = os.environ.get("OWNER_TAG", "silentalways07")
#Time in seconds for message delete, put 0 to never delete
TIME = int(os.environ.get("TIME", "0"))


#Shortner (token system) 
"""
some token verification sites
https://dashboard.shareus.io/
"""

# Turn this feature on or off using True or False put value inside  ""
# TRUE for yes FALSE if no 
USE_SHORTLINK = True if os.environ.get('USE_SHORTLINK', "False") == "True" else False 
# only shareus service known rightnow rest you can test on your own
SHORTLINK_API_URL = os.environ.get("SHORTLINK_API_URL", "Modijiurl.com")
# SHORTLINK_API_KEY = os.environ.get("SHORTLINK_API_KEY", "beb3b795a226177f3af7c937a2f01d5d7d4f4cf0")
#use this key if not working ☠️ (jokin!!)
SHORTLINK_API_KEY = os.environ.get("SHORTLINK_API_KEY", "beb3b795a226177f3af7c937a2f01d5d7d4f4cf0")
#add your custom time in secs for shortlink expiration.
# 24hr = 86400
# 12hr = 43200
VERIFY_EXPIRE = int(os.environ.get('VERIFY_EXPIRE', "60")) # Add time in seconds
#put TRUE if you want shortner in every link generated by the bot.
U_S_E_P = True if (True if os.environ.get('U_S_E_P', "False") == "True" else False) and (USE_SHORTLINK) else False
#Tutorial video for the user of your shortner on how to download.
TUT_VID = os.environ.get("TUT_VID","https://t.me/How_to_Download_7x/32")





#Payment to remove the token system
#put TRUE if you want this feature
USE_PAYMENT = False if (True if os.environ.get("USE_PAYMENT", "FALSE") == "TRUE" else False) and (USE_SHORTLINK) else False
#UPI_ID
UPI_ID = os.environ.get("UPI_ID", "rohit23pnb@axl")
#UPI QR CODE IMAGE
UPI_IMAGE_URL = os.environ.get("UPI_IMAGE_URL", "https://envs.sh/B7w.png")
#SCREENSHOT URL of ADMIN for verification of payments
SCREENSHOT_URL = os.environ.get("SCREENSHOT_URL", f"t.me/{OWNER_TAG}")
#Time and its price
#7 Days
PRICE1 = os.environ.get("PRICE1", "20 rs")
#1 Month
PRICE2 = os.environ.get("PRICE2", "49 rs")
#3 Month
PRICE3 = os.environ.get("PRICE3", "135 rs")
#6 Month
PRICE4 = os.environ.get("PRICE4", "250 rs")
#1 Year
PRICE5 = os.environ.get("PRICE5", "500 rs")



#force message for joining the channel
FORCE_MSG = os.environ.get("FORCE_MSG", "Hello {first}\n\n<b>You need to join in my Channel/Group to use me\n\nKindly Please join Channel</b> 🥺")
#custom caption 
CUSTOM_CAPTION = os.environ.get("CUSTOM_CAPTION", "<b>• ʙʏ @MANAGERR0007</b>")
#protected content so that no files can be sent from the bot to anyone. recommended False
# TRUE for yes FALSE if no
PROTECT_CONTENT = True if os.environ.get("PROTECT_CONTENT", "TRUE") == "TRUE" else False
#used if you dont need buttons on database channel.
# True for yes False if no
DISABLE_CHANNEL_BUTTON = True if os.environ.get("DISABLE_CHANNEL_BUTTON", "TRUE") == "TRUE" else False
#you can add admin inside the bot(bug right now will fix later)

try:
    ADMINS=[]
    for x in (os.environ.get("ADMINS", "7328629001 ").split()):
        ADMINS.append(int(x))
except ValueError:
        raise Exception("Your Admins list does not contain valid integers.")




#no need to add anything from now on

ADMINS.append(OWNER_ID)


LOG_FILE_NAME = "logs.txt"
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
