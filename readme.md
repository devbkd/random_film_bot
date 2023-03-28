Телеграм-бот, который предлагает случайный фильм или сериал пользователю. Когда пользователь 
нажимает на команду /start, бот отправляет сообщение с двумя кнопками - "Фильм" и "Сериал". 
После нажатия одной из кнопок бот случайным образом выбирает фильм или сериал из списка, который 
был загружен из файлов "data/movies.txt" и "data/series.txt".
Структура:
├── movies_series_bot.py
└── data
    ├── movies.txt
    └── series.txt

movies_series_bot.py - основной скрипт проекта.
data/movies.txt - текстовый файл с названиями фильмов, каждый фильм на новой строке.
data/series.txt - текстовый файл с названиями сериалов, каждый сериал на новой строке.
Код написан на Python 3.9.10 все используемые библиотеки указаны в requirements.txt. 
Для запуска данного проекта вам нужно:
1. Склонировать проект из репозитория.
2. Создать вирутальное окружение в директорий проекта. 
3. Активировать созданное виртуальное окружение.
4. Установить библиотеки с помощью файла requirements.txt (pip install -r requirements.txt).
5. Так же вам нужно создать бота в телеграме, получить token.
6. Создать файл .env в директорий проекта, и там указать TELEGRAM_TOKEN=ваш телеграм токен
7. Запустить проект.