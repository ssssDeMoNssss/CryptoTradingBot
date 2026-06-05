from telegram import Bot
import os

def send_notification(message):
    bot = Bot(token=os.getenv('TELEGRAM_TOKEN'))
    bot.send_message(chat_id=os.getenv('TELEGRAM_CHAT_ID'), text=message)
