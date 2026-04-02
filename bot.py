import os
import requests
from telegram.ext import Updater, MessageHandler, Filters

# Environment Variables (Railway से आएंगे)
BOT_TOKEN = os.getenv("8216878019:AAGI_UcfNgk0Y4XrLuf6SZwDocQgawSZ674")
API_KEY = os.getenv("AIzaSyBqV0Y4PmhhJoeqyU8pU-2okg9Pv-ofbH0")

def reply(update, context):
    user_message = update.message.text

    url = "https://api.openai.com/v1/chat/completions"
    
    headers = {
        "Authorization": f"Bearer {API_KEY}",
        "Content-Type": "application/json"
    }

    data = {
        "model": "gpt-4o-mini",
        "messages": [
            {"role": "system", "content": "You are a helpful AI assistant. Reply in Hindi and English."},
            {"role": "user", "content": user_message}
        ]
    }

    try:
        response = requests.post(url, headers=headers, json=data)
        result = response.json()

        reply_text = result['choices'][0]['message']['content']
    except Exception as e:
        reply_text = "Error aa gaya 😅\n" + str(e)

    update.message.reply_text(reply_text)

# Bot start
updater = Updater(BOT_TOKEN, use_context=True)
dp = updater.dispatcher

dp.add_handler(MessageHandler(Filters.text & ~Filters.command, reply))

print("🤖 Bot is running...")
updater.start_polling()
updater.idle()
