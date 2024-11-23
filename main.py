import telebot

token = '7875957494:AAETOpVDPAvG0rHulyutGqB0oI3aPcon7P4'
bot = telebot.TeleBot(token)


@bot.message_handler(content_types=['text'])
def test_text(message):
    print(message)

    msg = message.text + ' - this is a text message(це текстове повідомлення)'
    bot.send_message(message.chat.id, msg)



if __name__ == '__main__':
    bot.polling()
