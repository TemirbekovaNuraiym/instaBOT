import telebot
from telebot import types
import requests

token = '7179170524:AAFyAytOhlQH-hsYqOAz1aG2VFKz723RNdE'
bot = telebot.TeleBot(token)

@bot.message_handler(commands=['start'])
def start_message(message):
    bot.send_message(message.chat.id, """Привет! Я бот Instagram.
Нажмите на следующую команду для дальнейшей работы:
/inst""")

@bot.message_handler(commands=['inst'])
def button_message(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    item1 = types.KeyboardButton("Посты")
    item2 = types.KeyboardButton("Отзывы")
    item3 = types.KeyboardButton("Пользователи")
    markup.add(item1, item2, item3)
    bot.send_message(message.chat.id, 'Выберите что вам надо', reply_markup=markup)

@bot.message_handler(content_types=['text'])
def message_reply(message):
    if message.text == "Посты":
        response = requests.get('http://35.225.150.89/posts/')
        if response.status_code == 200:
            bot.send_message(message.chat.id, f'Информация о постах:\n{response.text}')
        else:
            bot.send_message(message.chat.id, 'Произошла ошибка при получении информации о постах.')
    elif message.text == "Отзывы":
        response = requests.get('http://35.225.150.89/review/')
        if response.status_code == 200:
            bot.send_message(message.chat.id, f'Информация об отзывах:\n{response.text}')
        else:
            bot.send_message(message.chat.id, 'Произошла ошибка при получении отзывов.')
    elif message.text == "Пользователи":
        response = requests.get('http://35.225.150.89/account/users/')
        if response.status_code == 200:
            bot.send_message(message.chat.id, f'Информация о пользователях:\n{response.text}')
        else:
            bot.send_message(message.chat.id, 'Произошла ошибка при получении информации о пользователях.')

bot.infinity_polling()
