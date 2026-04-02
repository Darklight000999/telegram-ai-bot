import os
import openai
from telegram.ext import Updater, MessageHandler, Filters

# ===============================
# 🔑 Keys
# ===============================
BOT_TOKEN = "8216878019:AAHMs-HkOf6cKLB__-bVBRBcSGLW8H-KB8A"
OPENAI_API_KEY = "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"

# OpenAI setup
openai.api_key = OPENAI_API_KEY

# ===============================
# 🟢 Telegram message handler
# ===============================
def handle_message(update, context):
    user_text = update.message.text

    # Prompt: user text + guidance for ethical hacking
    prompt = f"""
    You are an AI assistant specialized in ethical hacking guidance.
    Only provide legal commands and advice for learning/testing on systems you own or have permission.
    User asked: {user_text}
    Provide step-by-step guidance in simple text.
    """

    try:
        # OpenAI API call
        response = openai.Completion.create(
            model="text-davinci-003",
            prompt=prompt,
            max_tokens=200,
            temperature=0.5
        )

        # Get the text reply
        reply_text = response.choices[0].text.strip()
        update.message.reply_text(reply_text)

    except Exception as e:
        update.message.reply_text(f"⚠️ Error: {e}")

# ===============================
# 🟢 Telegram bot setup
# ===============================
updater = Updater(BOT_TOKEN, use_context=True)
dispatcher = updater.dispatcher

# Text messages handler
dispatcher.add_handler(MessageHandler(Filters.text & ~Filters.command, handle_message))

print("🤖 Telegram Text-Only AI Bot running...")
updater.start_polling()
updater.idle()
