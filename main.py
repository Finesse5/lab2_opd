import telebot
import os
import random
from telebot import types

# Токен вашего бота, полученный от BotFather в Telegram
TOKEN = '7119553272:AAHCDR1mZL_cdU1watRiNW-qDuxnyKZAQjY'

# Директория, в которой находятся мотивационные картинки
IMAGES_DIR = 'motivational_images'

# Создание объекта бота
bot = telebot.TeleBot(TOKEN)

# Получение списка файлов с мотивационными картинками
images = os.listdir(IMAGES_DIR)

# Обработчик команды /start
@bot.message_handler(commands=['start'])
def start_message(message):
    bot.send_message(message.chat.id, "Привет! Я генератор мотивационных картинок. Нажми на кнопку, чтобы получить мотивацию!", reply_markup=generate_markup())

# Генерация разметки с кнопкой "Получить мотивацию"
def generate_markup():
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    markup.add(types.KeyboardButton("Получить мотивацию"))
    return markup

# Обработчик нажатия на кнопку "Получить мотивацию"
@bot.message_handler(func=lambda message: True)
def send_motivational_image(message):
    if message.text == 'Получить мотивацию':
        # Выбор случайной мотивационной картинки
        image_name = random.choice(images)
        image_path = os.path.join(IMAGES_DIR, image_name)
        # Отправка мотивационной картинки
        with open(image_path, 'rb') as photo:
            bot.send_photo(message.chat.id, photo)
    else:
        bot.send_message(message.chat.id, "Нажми на кнопку, чтобы получить мотивацию!", reply_markup=generate_markup())

# Отслеживание обновлений от Telegram API с использованием Long Polling
bot.polling()
