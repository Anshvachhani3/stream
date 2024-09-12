import os
from os import getenv, environ
from dotenv import load_dotenv

load_dotenv()
bot_name = "ᴀɴs Fɪʟᴇ2Lɪɴᴋ Bᴏᴛ"
bisal_channel = "https://t.me/+aE7D-Fd-gBkyMjk1"
bisal_grp = "https://t.me/+aE7D-Fd-gBkyMjk1"

class Var(object):
    MULTI_CLIENT = False
    API_ID = int(getenv('API_ID', '8012239'))
    API_HASH = str(getenv('API_HASH', '171e6f1bf66ed8dcc5140fbe827b6b08'))
    BOT_TOKEN = str(getenv('BOT_TOKEN', '6271945413:AAFEHJ8NWdMliX5SkE0FuAsjJbFcT44OdtQ'))
    name = str(getenv('name', 'Ansh-Vachhani'))
    SLEEP_THRESHOLD = int(getenv('SLEEP_THRESHOLD', '60'))
    WORKERS = int(getenv('WORKERS', '4'))
    BIN_CHANNEL = int(getenv('BIN_CHANNEL', '-1001832234721'))
    NEW_USER_LOG = int(getenv('NEW_USER_LOG', '-1001832234721'))
    PORT = int(getenv('PORT', '8080'))
    BIND_ADRESS = str(getenv('WEB_SERVER_BIND_ADDRESS', '0.0.0.0'))
    PING_INTERVAL = int(environ.get("PING_INTERVAL", "1200"))  # 20 minutes
    OWNER_ID = [int(x) for x in os.environ.get("OWNER_ID", "5660839376").split()]
    NO_PORT = bool(getenv('NO_PORT', False))
    APP_NAME = None
    OWNER_USERNAME = str(getenv('OWNER_USERNAME', 'Legend_BoyCC'))
    
    if 'DYNO' in environ:
        ON_HEROKU = True
        APP_NAME = str(getenv('APP_NAME', 'ansh-vachhani'))  # Auto-filled based on VPS config
    else:
        ON_HEROKU = False

    FQDN = str(getenv('FQDN', 'http://vps.hostingup.icu:9097')) if not ON_HEROKU or getenv('FQDN', '') else APP_NAME + '.herokuapp.com'
    HAS_SSL = bool(getenv('HAS_SSL', True))
    
    if HAS_SSL:
        URL = "https://{}/".format(FQDN)
    else:
        URL = "http://{}/".format(FQDN)
    
    DATABASE_URL = str(getenv('DATABASE_URL', 'mongodb+srv://Ansh089:Ansh089@cluster0.y8tpouc.mongodb.net/?retryWrites=true&w=majority'))
    UPDATES_CHANNEL = str(getenv('UPDATES_CHANNEL', 'None')) 
    BANNED_CHANNELS = list(set(int(x) for x in str(getenv("BANNED_CHANNELS", "")).split()))   
    BAN_CHNL = list(set(int(x) for x in str(getenv("BAN_CHNL", "")).split()))   
    BAN_ALERT = str(getenv('BAN_ALERT', '<b>ʏᴏᴜ ᴀʀᴇ ʙᴀɴɴᴇᴅ ᴛᴏ ᴜsᴇ ᴛʜɪs ʙᴏᴛ. Pʟᴇᴀsᴇ ᴄᴏɴᴛᴀᴄᴛ @biisal_bot ᴛᴏ ʀᴇsᴏʟᴠᴇ ᴛʜᴇ ɪssᴜᴇ!!</b>'))
