import os
import requests
from telegram.ext import Updater, MessageHandler, Filters

# 🔑 Put your keys here
BOT_TOKEN = "8216878019:AAHMs-HkOf6cKLB__-bVBRBcSGLW8H-KB8A"
OPENAI_API_KEY = "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"

# Function to handle messages
def reply(update, context):
    user_message = update.message.text

    url = "https://api.openai.com/v1/chat/completions"
    headers = {
        "Authorization": f"Bearer {OPENAI_API_KEY}",
        "Content-Type": "application/json"
    }
    data = {
        "model": "gpt-4o-mini",
        "messages": [
            {"role": "system", "content": "You are a helpful AI assistant."},
            {"role": "user", "content": user_message}
        ]
    }

    try:
        response = requests.post(url, headers=headers, json=data)
        response_json = response.json()
        # Extract reply text
        reply_text = response_json['choices'][0]['message']['content']
    except Exception as e:
        reply_text = "Error: " + str(e)

    update.message.reply_text(reply_text)

# Set up the bot
updater = Updater(BOT_TOKEN, use_context=True)
dp = updater.dispatcher
dp.add_handler(MessageHandler(Filters.text & ~Filters.command, reply))

print("🤖 AI Bot is running...")
updater.start_polling()
updater.idle()
