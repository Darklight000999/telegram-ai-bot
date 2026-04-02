import os
import requests
from telegram.ext import Updater, MessageHandler, Filters

# ⚡ Directly put your keys here
BOT_TOKEN = "8216878019:AAHMs-HkOf6cKLB__-bVBRBcSGLW8H-KB8A"
API_KEY = "AIzaSyBqV0Y4PmhhJoeqyU8pU-2okg9Pv-ofbH0"

# Function to handle user messages
def reply(update, context):
    user_message = update.message.text

    # OpenAI API request
    url = "https://api.openai.com/v1/chat/completions"
    headers = {
        "Authorization": f"Bearer {API_KEY}",
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
        result = response.json()
        reply_text = result['choices'][0]['message']['content']
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
