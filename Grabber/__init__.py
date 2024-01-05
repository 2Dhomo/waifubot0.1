import logging  

from pyrogram import Client 

from telegram.ext import Application
from motor.motor_asyncio import AsyncIOMotorClient

logging.basicConfig(
    format="%(asctime)s - %(levelname)s - %(name)s - %(message)s",
    handlers=[logging.FileHandler("log.txt"), logging.StreamHandler()],
    level=logging.INFO,
)

logging.getLogger("apscheduler").setLevel(logging.ERROR)
logging.getLogger('httpx').setLevel(logging.WARNING)
logging.getLogger("pyrate_limiter").setLevel(logging.ERROR)
LOGGER = logging.getLogger(__name__)

OWNER_ID = "1005344893"
sudo_users = ["1005344893", "6890857225"]
GROUP_ID = "-1002112492698"
TOKEN = "6872955784:AAGZQZu-rsAyFipm2Cz0FiyPjFl2Lz2PhJA"
mongo_url = "mongodb+srv://tiwarireeta004:YJyL0ZdPfvF7Dyho@cluster0.md4bpdh.mongodb.net/?retryWrites=true&w=majority"
PHOTO_URL = ["https://telegra.ph/file/adb19b3c948b77eb24101.jpg"]
SUPPORT_CHAT = "WaifuCatherSupport"
UPDATE_CHAT = "Grabers_World"
BOT_USERNAME = "WaifuCatherUpdate"
CHARA_CHANNEL_ID = "-1002096911233"
api_id = "20457610"
api_hash = "b7de0dfecd19375d3f84dbedaeb92537"

application = Application.builder().token(TOKEN).build()
Grabberu = Client("Grabber", api_id, api_hash, bot_token=TOKEN)
client = AsyncIOMotorClient(mongo_url)
db = client['Character_catcher']
collection = db['anime_characters']
user_totals_collection = db['user_totals']
user_collection = db["user_collection"]
group_user_totals_collection = db['group_user_total']
top_global_groups_collection = db['top_global_groups']
