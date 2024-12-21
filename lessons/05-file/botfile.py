from os import write

import telebot

token = '7991465200:AAF-y2rC0pO6Qqhak89IeKrG8TbX2vp8V7c'
bot = telebot.TeleBot(token)

def f1(v):
    try:
        int(v)
        return True
    except ValueError:
        return False

@bot.message_handler(content_types=['text'])
def is_text(message):
    if not f1(message.text):
        filename = 'bot_text.txt'
    else:
        filename = 'bot_number.txt'

    with open(filename, 'a') as file:
        file.write(message.text + '\n')


    bot.send_message(message.chat.id, 'Збережено до файла!')

if __name__ == '__main__':
    bot.polling()