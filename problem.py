import requests
import telebot
import bs4  # BeautifulSoup4
from telebot import types
from io import BytesIO

def get_quote():

    anime = ''
    character = ''
    quote = ''
    #https://animechan.vercel.app/api/random
    req = requests.get('https://random.dog/woof.json')
    if req.status_code == 200:
        r_json = req.json()
        anime = r_json["anime"]
        # url.split("/")[-1]
    return anime

