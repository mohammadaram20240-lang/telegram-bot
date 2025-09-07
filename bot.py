import telebot

# توکن ربات (که از BotFather گرفتی)
TOKEN = "8167705643:AAHOuJekHbSobdaKrXCEP5jx4s3BQFgX0_U"
bot = telebot.TeleBot(TOKEN)

# وقتی کاربر /start بزند
@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.reply_to(message, "سلام ✨ به ربات خوش اومدی!")

# اجرای ربات
bot.polling()