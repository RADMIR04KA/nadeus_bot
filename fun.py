# ======================================= Развлечения
import requests
import telebot
import bs4  # BeautifulSoup4
from telebot import types
from io import BytesIO
import secret  # секретные ключи, пароли
bot = telebot.TeleBot("5123164493:AAEmHYCyVvKt7-IiZTYqZC7ssbZCFMZ5U5A")
# -----------------------------------------------------------------------
def get_text_messages(bot, cur_user, message):
    chat_id = message.chat.id
    ms_text = message.text



    if ms_text == "Прислать лису":
        bot.send_photo(chat_id, photo=get_foxURL(), caption="Вот тебе лисичка!")

    elif ms_text == "Прислать анекдот":
        bot.send_message(chat_id, text=get_anekdot())

    elif ms_text == "Прислать новости":
        bot.send_message(chat_id, text=get_news())

    elif ms_text == "Прислать фильм":
        send_film(bot, chat_id)

    elif ms_text == "Угадай кто?":
        get_ManOrNot(bot, chat_id)

    elif ms_text == "Прислать курсы":
        bot.send_message(chat_id, text=get_cur())





# -----------------------------------------------------------------------
def get_fox():
    url = ""
    r = requests.get('https://randomfox.ca/floof/')
    if r.status_code == 200:
        r_json = r.json()
        url = r_json['image']
    return url


# -----------------------------------------------------------------------
def get_anekdot():
    array_anekdots = []
    req_anek = requests.get('https://www.anekdot.ru/random/anekdot/')
    if req_anek.status_code == 200:
        soup = bs4.BeautifulSoup(req_anek.text, "html.parser")
        result_find = soup.select('.text')
        for result in result_find:
            array_anekdots.append(result.getText().strip())
    if len(array_anekdots) > 0:
        return array_anekdots[0]
    else:
        return ""


#------------------------------------



def get_fact():
    array_fact = []
    req_fact = requests.get('https://randstuff.ru/fact/')
    if req_fact.status_code == 200:
        soup = bs4.BeautifulSoup(req_fact.text, "html.parser")
        result_find = soup.select('.text')
        for result in result_find:
            array_fact.append(result.getText().strip())
    if len(array_fact) > 0:
        return array_fact[0]
    else:
        return ""
# -----------------------------------------------------------------------
def get_news():
    array_anekdots = []
    req_anek = requests.get('https://www.banki.ru/news/lenta')
    if req_anek.status_code == 200:
        soup = bs4.BeautifulSoup(req_anek.text, "html.parser")
        result_find = soup.select('.doFpcq')
        for result in result_find:
            print(result)

            # array_anekdots.append(result.getText().strip())
    if len(array_anekdots) > 0:
        return array_anekdots[0]
    else:
        return ""


# -----------------------------------------------------------------------

def get_foxURL():
    url = ""
    req = requests.get('{"image":"https:\/\/randomfox.ca\/images\/46.jpg","link":"https:\/\/randomfox.ca\/?i=46"}')
    if req.status_code == 200:
        r_json = req.json()
        url = r_json['image']
        # url.split("/")[-1]
    return url


# -----------------------------------------------------------------------

def get_quote():
    texta = ''

    #https://animechan.vercel.app/api/random
    req = requests.get('https://animechan.vercel.app/api/random')
    if req.status_code == 200:
        data = req.json()
        anime = data['anime']
        character = data['character']
        quote = data['quote']
        texta += f'Аниме: {anime}\n'
        texta += f'Персонаж: {character}\n'
        texta += f'Цитата: {quote}'

    return texta


# -----------------------------------------------------------------------

def get_cur_pairs():
    lst_cur_pairs = []
    req_currency_list = requests.get(f'https://currate.ru/api/?get=currency_list&key={SECRET.CURRATE_RU}')
    if req_currency_list.status_code == 200:
        currency_list_json = req_currency_list.json()
        for pairs in currency_list_json["data"]:
            if pairs[3:] == "RUB":
                lst_cur_pairs.append(pairs)
    return lst_cur_pairs


# -----------------------------------------------------------------------
def get_cur():
    txt_curses = ""
    txt_pairs = ",".join(get_cur_pairs())
    req_currency_rates = requests.get(f'https://currate.ru/api/?get=rates&pairs={txt_pairs}&key={SECRET.CURRATE_RU}')
    if req_currency_rates.status_code == 200:
        currency_rates = req_currency_rates.json()
        for pairs, rates in currency_rates["data"].items():
            txt_curses += f"{pairs} : {rates}\n"
    else:
        txt_curses = req_currency_rates.text
    return txt_curses


# -----------------------------------------------------------------------
def get_ManOrNot(chat_id):
    global bot

    markup = types.InlineKeyboardMarkup()
    btn1 = types.InlineKeyboardButton(text="Проверить", url="https://vc.ru/dev/58543-thispersondoesnotexist-sayt-generator-realistichnyh-lic")
    markup.add(btn1)

    req = requests.get("https://thispersondoesnotexist.com/image", allow_redirects=True)
    if req.status_code == 200:
        img = BytesIO(req.content)
        bot.send_photo(chat_id, photo=img, reply_markup=markup, caption="Этот человек реален?")

# ---------------------------------------------------------------------

