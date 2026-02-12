# config.py

import os

from dotenv import load_dotenv

load_dotenv()

# Базовая директория проекта
BASE_DIR = os.path.dirname(os.path.abspath(__file__))

# Временная директория для хранения загруженных видео
TEMP_DIRECTORY = os.path.join(BASE_DIR, "temp_videos")
BOT_TOKEN = os.getenv("BOT_TOKEN")

# Server configuration
PORT = int(os.getenv("PORT", "8000"))  # Default port 8000 if not specified
HOST = os.getenv("HOST", "0.0.0.0")   # Default host 0.0.0.0 if not specified

# Webhook / polling configuration
# USE_WEBHOOK = "true" (default) -> pakai webhook
# USE_WEBHOOK = "false"          -> pakai long polling (tanpa webhook)
USE_WEBHOOK = os.getenv("USE_WEBHOOK", "true").lower() == "true"

# Webhook configuration (dipakai hanya jika USE_WEBHOOK = True)
# Default path jika tidak diset di environment, supaya tidak None di Koyeb
WEBHOOK_PATH = os.getenv("WEBHOOK_PATH", "/webhook")
WEBHOOK_URL = os.getenv("WEBHOOK_URL")

# MongoDB configuration
MONGODB_URI = os.getenv("MONGODB_URI")
MONGODB_DB_NAME = os.getenv("MONGODB_DB_NAME")
MONGODB_USERS_COLLECTION = os.getenv("MONGODB_USERS_COLLECTION")

# User management configuration
ADMIN_IDS = list(map(int, filter(None, os.getenv("ADMIN_IDS", "").split(","))))

# Channel to store backup of all downloaded files (optional)
# Set DATABASE_CHANNEL_ID to a Telegram channel ID (with bot added as admin)
DATABASE_CHANNEL_ID = int(os.getenv("DATABASE_CHANNEL_ID", "0") or "0")




# Dictionary for identifying platform based on URL - Top 10 most popular platforms
PLATFORM_IDENTIFIERS = {
    # Top Social Media & Video Platforms (by global usage)
    "youtube.com": "YouTube",
    "youtu.be": "YouTube",
    "instagram.com": "Instagram",
    "tiktok.com": "TikTok",
    "facebook.com": "Facebook",
    "fb.com": "Facebook",
    "twitter.com": "Twitter",
    "x.com": "Twitter",
    "pinterest.com": "Pinterest",
    "pin.it": "Pinterest",
    "reddit.com": "Reddit",
    "vimeo.com": "Vimeo",
}
