import telebot  # pyTelegramBotAPI 4.3.1

bot = telebot.TeleBot("5123164493:AAEmHYCyVvKt7-IiZTYqZC7ssbZCFMZ5U5A")
@bot.message_handler(commands=['start'])
def welcome(message):
    mesg = bot.send_message(message.chat.id,'Please send me message')
    bot.register_next_step_handler(mesg,test)


def test(message):
    bot.send_message(message.chat.id,'You send me message')