import telebot
from telebot import types

bot = telebot.TeleBot("5123164493:AAEmHYCyVvKt7-IiZTYqZC7ssbZCFMZ5U5A")

@bot.message_handler(commands=['start'])
def start(message):
    mess = f'Hi, <b><u>{message.from_user.username}</u></b>'
    bot.send_message(message.chat.id, mess, parse_mode='html')

@bot.message_handler()
def get_u_t(message): #get_user_text

    bot.send_message(message.chat.id, message)

@bot.message_handler(content_types=['photo'])
def get_u_p(photo): #get_user_photo
    bot.send_message(photo.chat.id, f'Ого, прикольное фото', parse_mode='html')

@bot.message_handler(commands=['Vk'])
def website(messege):
    markup = types.InlineKeyboardMarkup()
    markup.add(types.InlineKeyboardButton('Vk', url='https://vk.com/heyfroise'))
    bot.send_message(messege.chat.id, f'зайти на страницу Vk', reply_markup=markup)

@bot.message_handler(commands=['help'])
def buttons(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=1)   #resize_keyboard=True - кнопки подстраивают размер, row_width=1 - количество кнопок в ряду
    website = types.KeyboardButton('website')
    start = types.KeyboardButton('start')
    markup.add(website, start)
    bot.send_message(message.chat.id, 'меню помощи', reply_markup=markup)




bot.polling(none_stop=True)