
from io import BytesIO
from SECRET import OWM
import telebot  # pyTelegramBotAPI 4.3.1
from telebot import types

from Weather import mainOWM, get_weather
from DZ import my_input
import DZ
import botGames
from botmenu import Menu
from fun import get_anekdot, get_fact, get_fox, get_ManOrNot, get_quote
from botmenu import Users
from telebot import types
from SECRET import OWM
import requests
from pprint import pprint

bot = telebot.TeleBot("5123164493:AAEmHYCyVvKt7-IiZTYqZC7ssbZCFMZ5U5A")

@bot.message_handler(commands=['start'])
def start(message, res=False):
    chat_id = message.chat.id
    mess = f'<b>Привет, <u>{message.from_user.username}</u>. Я бот созданный зачета по программированию, мое имя ProBot. Ты находишься в главном меню. </b>'
    bot.send_message(chat_id, text=mess, parse_mode='html', reply_markup=Menu.getMenu(chat_id, "Главное меню").markup)

@bot.message_handler(content_types=['text'])
def get_text_messages(message):

    chat_id = message.chat.id
    ms_text = message.text

    cur_user = Users.getUser(chat_id)
    if cur_user == None:
        cur_user = Users(chat_id, message.json["from"])

    result = goto_menu(chat_id, ms_text)  # попытаемся использовать текст как команду меню, и войти в него
    if result == True:
        return  # мы вошли в подменю, и дальнейшая обработка не требуется

    cur_menu = Menu.getCurMenu(chat_id)
    if cur_menu != None and ms_text in cur_menu.buttons:  # проверим, что команда относится к текущему меню

        if ms_text == "Помощь":
            send_help(chat_id)

        elif ms_text == "Прислать факт":
            bot.send_message(chat_id, text=get_fact())

        elif ms_text == "Прислать анекдот":
            bot.send_message(chat_id, text=get_anekdot())

        elif ms_text == "Прислать фильм":
            send_film(chat_id)


        elif ms_text == "Прислать цитату":
            bot.send_message(chat_id, text=get_quote())

        elif ms_text == "Прислать лису":
            bot.send_photo(chat_id, photo=get_fox(), caption='Держи лисичку')

        elif ms_text == "Прислать аниме":
            get_randomAnime(chat_id)

        elif ms_text == "Угадай кто?":
            get_ManOrNot(chat_id)

        elif ms_text == "Прогноз погоды":


                def get_weather(OWM):
                    try:
                        bot.send_message(chat_id, text='Погода в городе СПб')
                        gorod = 'saintpetersburg'
                        r = requests.get(
                            f'https://api.openweathermap.org/data/2.5/weather?q={gorod}&appid=d9028bd837a2f592c7f6920a3c62710f&units=metric'
                        )
                        #my_input(bot, chat_id, "Moscow", r)
                        data = r.json()
                        pprint(r)

                        sity = data['name']
                        cur_weather = data['main']['temp']
                        humidity = data['main']['humidity']
                        pressure = data['main']['pressure']
                        wind = data['wind']['speed']

                        bot.send_message(chat_id, text=f'погода в городе: {sity} \nТемпература: {cur_weather}С\n'
                                    f'Влажность: {humidity}%\nДавление: {pressure} мм.рт.ст\nВетер: {wind}м/с\n')
                    except Exception as e:
                        bot.send_message(chat_id, text=e)
                        bot.send_message(chat_id, text=r)
                        bot.send_message(chat_id, text=ms_text)
                        bot.send_message(chat_id, text=OWM)

                #gorod  = ms_text
                #msg =
                #bot.register_next_step_handler(msg, get_weather)


        elif ms_text == "Карту!":
            game21 = botGames.getGame(chat_id)
            if game21 == None:  # если мы случайно попали в это меню, а объекта с игрой нет
                goto_menu(chat_id, "Выход")
                return

            text_game = game21.get_cards(1)
            bot.send_media_group(chat_id, media=getMediaCards(game21))  # получим и отправим изображения карт
            bot.send_message(chat_id, text=text_game)

            if game21.status != None:  # выход, если игра закончена
                botGames.stopGame(chat_id)
                goto_menu(chat_id, "Выход")
                return

        elif ms_text == "Стоп!":
            botGames.stopGame(chat_id)
            goto_menu(chat_id, "Выход")
            return

        elif ms_text == "Задание-1":
            DZ.dz1(bot, chat_id)

        elif ms_text == "Задание-2":
            DZ.dz2(bot, chat_id)

        elif ms_text == "Задание-3":
            DZ.dz3(bot, chat_id)

        elif ms_text == "Задание-4":
            DZ.dz4(bot, chat_id)

        elif ms_text == "Задание-5":
            DZ.dz5(bot, chat_id)

        elif ms_text == "Задание-6":
            DZ.dz6(bot, chat_id)

        elif ms_text == "Задание-7":
            DZ.dz7(bot, chat_id)

    else:  # ...........................................................................................................
        bot.send_message(chat_id, text="Мне жаль, я не понимаю вашу команду: " + ms_text)
        goto_menu(chat_id, "Главное меню")


def send_help(chat_id):
    global bot
    bot.send_message(chat_id, "Автор: Radmir Finogeev")
    markup = types.InlineKeyboardMarkup(row_width=1)
    btn1 = types.InlineKeyboardButton(text='Vk', url='https://vk.com/heyfroise')
    btn2 = types.InlineKeyboardButton(text='Tg', url='https://t.me/FROISE')
    markup.add(btn1, btn2)
    img = open('mirka.jpg', 'rb')
    bot.send_photo(chat_id, img, reply_markup=markup)

    bot.send_message(chat_id, "Активные пользователи чат-бота:")
    for el in Users.activeUsers:
        bot.send_message(chat_id, Users.activeUsers[el])





@bot.callback_query_handler(func=lambda call: True)
def callback_worker(call):
    # если требуется передать параметр или несколько параметров в обработчик кнопки, использовать методы Menu.getExtPar() и Menu.setExtPar()
    pass
    # if call.data == "ManOrNot_GoToSite": #call.data это callback_data, которую мы указали при объявлении InLine-кнопки
    #
    #     # После обработки каждого запроса нужно вызвать метод answer_callback_query, чтобы Telegram понял, что запрос обработан.
    #     bot.answer_callback_query(call.id)




def goto_menu(chat_id, name_menu):
    # получение нужного элемента меню
    cur_menu = Menu.getCurMenu(chat_id)
    if name_menu == "Выход" and cur_menu != None and cur_menu.parent != None:
        target_menu = Menu.getMenu(chat_id, cur_menu.parent.name)
    else:
        target_menu = Menu.getMenu(chat_id, name_menu)

    if target_menu != None:
        bot.send_message(chat_id, text=target_menu.name, reply_markup=target_menu.markup)

        # Проверим, нет ли обработчика для самого меню. Если есть - выполним нужные команды
        if target_menu.name == "Игра в 21":
            game21 = botGames.newGame(chat_id, botGames.Game21(jokers_enabled=True))  # создаём новый экземпляр игры
            text_game = game21.get_cards(2)  # просим 2 карты в начале игры
            bot.send_media_group(chat_id, media=getMediaCards(game21))  # получим и отправим изображения карт
            bot.send_message(chat_id, text=text_game)

        return True
    else:
        return False
def getMediaCards(game21):
    medias = []
    for url in game21.arr_cards_URL:
        medias.append(types.InputMediaPhoto(url))
    return medias



def send_film(chat_id):
    film = get_randomFilm()
    info_str = f"<b>{film['Наименование']}</b>\n" \
               f"Год: {film['Год']}\n" \
               f"Страна: {film['Страна']}\n" \
               f"Жанр: {film['Жанр']}\n" \
               f"Продолжительность: {film['Продолжительность']}"
    markup = types.InlineKeyboardMarkup()
    btn1 = types.InlineKeyboardButton(text="Трейлер", url=film["Трейлер_url"])
    btn2 = types.InlineKeyboardButton(text="СМОТРЕТЬ онлайн", url=film["фильм_url"])
    markup.add(btn1, btn2)
    bot.send_photo(chat_id, photo=film['Обложка_url'], caption=info_str, parse_mode='HTML', reply_markup=markup)

# -----------------------------------------------------------------------
#потом удалить все что ниже




#удалить все что выше

bot.polling(none_stop=True, interval=0)