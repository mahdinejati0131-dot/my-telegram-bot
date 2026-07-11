import telebot

TOKEN = '8800613146:AAEaDznhFmIiOM_iJBAdOkqCBDlsV8r96Iw'
bot = telebot.TeleBot(TOKEN)

# پاک کردن وب‌هوک قبلی برای رفع خطا
bot.delete_webhook()

TECH_FILE_ID = 'AgADbQsAArcL2VE'

@bot.message_handler(commands=['start'])
def start(message):
    bot.reply_to(message, "سلام! نام کتاب را بنویس.")

@bot.message_handler(func=lambda message: message.text == "تکنولوژی آموزشی")
def send_tech(message):
    bot.send_document(message.chat.id, TECH_FILE_ID)

bot.polling()
