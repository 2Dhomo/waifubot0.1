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

OWNER_ID = "1375777824"
sudo_users = ["1375777824", "6642960731", "5827485348", "1669380723", "5892808263", "6355138450", "6695953903"]
GROUP_ID = "-1002029882944"
TOKEN = "6714477044:AAFSHwO-kEhB8-ljjvBg0AXFgxDr_kWtIR8"
mongo_url = "mongodb+srv://freepremiumy50:x119eJ2WE6lOyLZD@cluster0.qwcdkrj.mongodb.net/?retryWrites=true&w=majority"
PHOTO_URL = ["https://graph.org/file/f7d332878278443e9dae5.jpg"]
SUPPORT_CHAT = "Grabers_World"
UPDATE_CHAT = "Grabers_World"
BOT_USERNAME = "WaifuXBharatBot"
CHARA_CHANNEL_ID = "-1002057344180"
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
