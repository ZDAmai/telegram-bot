import pip

from background import keep_alive  # Импорт функции для поддержки работоспособности

pip.main(['install', 'pytelegrambotapi'])
import random
import time

import telebot

# Уникальный токен, полученный от BotFather
TOKEN = '7234911976:AAEBF0bIaGiqYFTTobiTtWm3vOGdvhV407k'
CHANNEL_ID = '@romikchlenik'  # Или ID канала, куда бот будет отправлять сообщения

# Список возможных сообщений
MESSAGES = [
    "УЛЬТРА",
    "ОГРОМНЫЙ",
    "НО",
    "КРИВОЙ",
    "ПИПОН"
]

bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=['start'])
def startBot(message):
    first_mess = f"<b>{message.from_user.first_name} {message.from_user.last_name}</b>, привет! Бот будет публиковать сообщения каждые 30 секунд."
    bot.send_message(message.chat.id, first_mess, parse_mode='html')

def publish_message():
    while True:
        try:
            # Генерация случайного сообщения
            message = random.choice(MESSAGES)
            bot.send_message(CHANNEL_ID, message)
            print(f'Successfully sent message to {CHANNEL_ID}')
        except Exception as e:
            print(f'Failed to send message: {e}')
        time.sleep(60)  # Ждём 30 секунд перед отправкой следующего сообщения

import threading

threading.Thread(target=publish_message).start()

keep_alive()  # Запускаем Flask-сервер в отдельном потоке
bot.polling(non_stop=True, interval=0)  # Запуск бота
