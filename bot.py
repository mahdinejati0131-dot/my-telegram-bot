import telebot

TOKEN = '8800613146:AAGQQY2W617D6pbWyCVpo1Lt0OnNkQKkJMM'
bot = telebot.TeleBot(TOKEN)

TECH_FILE_ID = 'AgADbQsAArcL2VE'

@bot.message_handler(commands=['start'])
def start(message):
    bot.reply_to(message, "سلام! نام کتاب را بنویس.")

@bot.message_handler(func=lambda message: message.text == "تکنولوژی آموزشی")
def send_tech(message):
    bot.send_document(message.chat.id, TECH_FILE_ID)

bot.infinity_polling()
