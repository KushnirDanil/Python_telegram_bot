import telebot

token = '7991465200:AAF-y2rC0pO6Qqhak89IeKrG8TbX2vp8V7c'
bot = telebot.TeleBot(token)

@bot.message_handler(content_types=['text'])
def is_text(message):
    bot.send_message(message.chat.id, message.text + '\n[Бот Працює]')

if __name__ == '__main__':
    bot.polling()