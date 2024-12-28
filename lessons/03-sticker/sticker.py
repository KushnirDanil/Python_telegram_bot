import telebot
from telebot import types
import os

token = "7991465200:AAF-y2rC0pO6Qqhak89IeKrG8TbX2vp8V7c"
bot = telebot.TeleBot(token)

# stickers
list_sticker = [
    'CAACAgIAAxkBAAO3Z0iqLLOSpaCz8_EVHM7uWxrxLD4AAgUAA8A2TxP5al-agmtNdTYE'
]


@bot.message_handler(content_types=['sticker'])
def handle_sticker(message):
    # print(message.sticker)
    # Отримуємо інформацію про стікер
    sticker_id = message.sticker.file_id
    emoji = message.sticker.emoji
    bot.reply_to(message, f"Ви надіслали стікер з емоджі {emoji} (ID: {sticker_id})")


@bot.message_handler(commands=['send_sticker'])
def my_send_sticker(message):
    bot.send_sticker(message.chat.id, list_sticker[0])


# --- content_types = text ----------------------------------------------------
@bot.message_handler(content_types=['text'])
def bot_message_text(message):
    if message.text == 'dog':
        current_file_path = os.path.abspath(__file__)
        current_directory = os.path.dirname(current_file_path)
        my_file_directory = os.path.join(current_directory, 'sticker', 'dog.webm')

        with open(my_file_directory, "rb") as sticker:
            bot.send_sticker(message.chat.id, sticker)

    else:
        # print(message)
        bot.send_message(message.chat.id, message.text + '... Text work!')


if __name__ == '__main__':
    bot.infinity_polling()
