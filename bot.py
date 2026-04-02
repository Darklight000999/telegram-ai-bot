import requests
from telegram.ext import Updater, MessageHandler, Filters

# 🔑 Keys
BOT_TOKEN = "8216878019:AAHMs-HkOf6cKLB__-bVBRBcSGLW8H-KB8A"
GEMNI_API_KEY = "AIzaSyBqV0Y4PmhhJoeqyU8pU-2okg9Pv-ofbH0"

# Function to generate Gemni video
def generate_video(update, context):
    user_text = update.message.text

    url = "https://api.gemni.ai/v1/generate"  # hypothetical endpoint
    headers = {"Authorization": f"Bearer {GEMNI_API_KEY}"}
    data = {
        "text": user_text,
        "character": "your_character_name",  # replace with your AI character
        "style": "head_and_hands_only",      # move head and hands only
        "background": "static"               # keep background static
    }

    try:
        response = requests.post(url, headers=headers, json=data)
        result = response.json()
        video_url = result.get("video_url")

        if video_url:
            update.message.reply_text(f"Here is your AI video: {video_url}")
        else:
            update.message.reply_text("Video generate नहीं हुआ, try again!")
    except Exception as e:
        update.message.reply_text(f"Error: {e}")

# Setup Telegram bot
updater = Updater(BOT_TOKEN, use_context=True)
dp = updater.dispatcher
dp.add_handler(MessageHandler(Filters.text & ~Filters.command, generate_video))

print("🤖 Gemni AI Bot is running...")
updater.start_polling()
updater.idle()
