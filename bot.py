import telebot
import os

TOKEN = '8800613146:AAEaDznhFmIiOM_iJBAdOkqCBDlsV8r96Iw'
bot = telebot.TeleBot(TOKEN)

TECH_FILE_ID = 'AgADbQsAArcL2VE'

@bot.message_handler(commands=['start'])
def start(message):
    bot.reply_to(message, "سلام! نام کتاب را بنویس.")

@bot.message_handler(func=lambda message: message.text == "تکنولوژی آموزشی")
def send_tech(message):
    bot.send_document(message.chat.id, TECH_FILE_ID)

# حذف polling و استفاده از روش ساده‌تر برای سرور
if __name__ == "__main__":
    bot.remove_webhook()
    bot.polling(none_stop=True)
