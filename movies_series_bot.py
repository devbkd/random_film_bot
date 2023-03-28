import logging
import os
import random
import sys
from logging.handlers import RotatingFileHandler

import telebot
from dotenv import load_dotenv
from telebot import types

load_dotenv()

TELEGRAM_TOKEN = os.getenv('TELEGRAM_TOKEN')
CLICK = (
    'Нажми:\nФильм — для получения названия фильма.\n'
    'Сериал — для получения названия сериала.'
)
ERROR_EXIT_CODE = 1
user_last_call_time = {}
data = {
    'movies': [],
    'series': [],
}


def read_file(file_path):
    with open(file_path, 'r', encoding='UTF-8') as f:
        return f.read().split('\n')


data['movies'] = read_file('data/movies.txt')
data['series'] = read_file('data/series.txt')

bot = telebot.TeleBot(TELEGRAM_TOKEN)


logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.ERROR,
    handlers=[
        logging.StreamHandler(stream=sys.stdout),
        RotatingFileHandler(
            __file__ + '.error.log',
            maxBytes=50000000,
            backupCount=5,
            encoding='utf-8',
        ),
    ],
)


@bot.message_handler(commands=['start'])
def start(message):
    """Отправляет пользователю сообщение с кнопками."""
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    movies_button = types.KeyboardButton("Фильм")
    series_button = types.KeyboardButton("Сериал")
    markup.add(movies_button)
    markup.add(series_button)
    try:
        bot.send_message(
            message.chat.id,
            f'{CLICK}',
            reply_markup=markup,
        )
    except Exception as e:
        logging.error(str(e))


@bot.message_handler(content_types=['text'])
def handler_text(message):
    """Отправляет случайный фильм или сериал пользователю."""
    categories = (('фильм', 'movies'), ('сериал', 'series'))
    try:
        for key, value in categories:
            if message.text.lower() == key:
                answer = random.choice(data[value])
    except KeyError:
        answer = f'Неправильная команда. Попробуйте еще раз.\n{CLICK}'
    try:
        bot.send_message(message.chat.id, answer)
    except Exception as e:
        logging.error(str(e))


if __name__ == '__main__':
    try:
        bot.infinity_polling(none_stop=True)
    except KeyboardInterrupt:
        bot.stop_polling()
        logging.info('Bot stopped')
        sys.exit()
    except Exception as e:
        logging.error(str(e))
        bot.stop_polling()
        logging.info('Bot stopped due to an error')
        sys.exit(ERROR_EXIT_CODE)
