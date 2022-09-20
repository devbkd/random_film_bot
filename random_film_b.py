import telebot                  # подключаем модуль для работы с телеграм
import config                           
import random                   # модуль для рандомного выбора
from telebot import types

#для хранения файлов со списками создаем отдельную папку data
f = open('data/films.txt', 'r', encoding='UTF-8')       # открываем файл со списком фильмов
films = f.read().split('\n')                            # чистаем файл
f.close()

f = open('data/serials.txt', 'r', encoding='UTF-8')     # открываем файл со списком сериалов
serials = f.read().split('\n')                          #
f.close()
# Создаем бота
bot = telebot.TeleBot(config.TOKEN)#рядом создаем отдельный файл(например: config) с расширением py, где будет хранится токен телеграм
# Команда start
@bot.message_handler(commands=["start"])
def start(m, res=False):
        # Добавляем две кнопки
        markup=types.ReplyKeyboardMarkup(resize_keyboard=True)
        item1=types.KeyboardButton("Фильм")
        item2=types.KeyboardButton("Сериал")
        markup.add(item1)
        markup.add(item2)
        bot.send_message(m.chat.id, 'Нажми: Фильм для получения названия фильма\nСериал — для получения названия сериала ',  reply_markup=markup)
# Получение сообщений от юзера
@bot.message_handler(content_types=["text"])
def handle_text(message):
    # Если юзер прислал 1, выдаем ему случайный факт
    if message.text.strip() == 'Фильм' :
            answer = random.choice(films)
    # Если юзер прислал 2, выдаем умную мысль
    elif message.text.strip() == 'Сериал':
            answer = random.choice(serials)
    # Отсылаем юзеру сообщение в его чат
    bot.send_message(message.chat.id, answer)
# Запускаем бота
bot.polling(none_stop=True, interval=0)

