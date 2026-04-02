import requests
import os
from telegram.ext import Updater, MessageHandler, Filters

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
            {"role": "system", "content": "You are a helpful AI assistant."},
            {"role": "user", "content": user_message}
        ]
    }

    response = requests.post(url, headers=headers, json=data)
    result = response.json()

    reply_text = result['choices'][0]['message']['content']
    update.message.reply_text(reply_text)

updater = Updater(8216878019:AAGI_UcfNgk0Y4XrLuf6SZwDocQgawSZ674, use_context=True)
dp = updater.dispatcher

dp.add_handler(MessageHandler(Filters.text, reply))

updater.start_polling()
updater.idle()
