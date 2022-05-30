from SECRET import OWM
import requests
from pprint import pprint


def get_weather(OWM):
    try:

        # pprint(data)

        city = data['name']
        cur_weather = data['main']['temp']
        humidity = data['main']['humidity']
        pressure = data['main']['pressure']
        wind = data['wind']['speed']

        bot.send_message(chat_id, text=f'погода в городе: {city} \nТемпература: {cur_weather}С\n'
                                       f'Влажность: {humidity}%\nДавление: {pressure} мм.рт.ст\nВетер: {wind}м/с\n')
    except Exception as e:
        bot.send_message(chat_id, text=e)
        bot.send_message(chat_id, text=r)

def mainOWM():
    city = input('ujhjl')
    get_weather(city, OWM)

if __name__ == "__main__":
    mainOWM()