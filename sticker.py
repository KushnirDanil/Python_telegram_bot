from pyexpat.errors import messages

import telebot
import os
from flask import flask, render_template
from flask_sqlalchemy import SQLAlchemy


token = '7991465200:AAF-y2rC0pO6Qqhak89IeKrG8TbX2vp8V7c'
bot = telebot.TeleBot(token)

app = flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///example.sqlite"

db = SQLAlchemy(app)


class Base(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    text = db.Column(db.String(), nubllable=False)

@app.route('/')
def index():
    mes = Base.query.all()
    return render_template('index.html', mes=mes)


sticker_list = [
    'CAACAgIAAxkBAAMfZ1QqGH1Viq7naanM5Ux_DU-meL8AAvsAA5i_gA0qWK0ODEDTQzYE',
    'CAACAgIAAxkBAAMhZ1QqG_VYmZq-tQg1PxLfWHFYK_oAAvYAA5i_gA071RmfH5IrQDYE',
    'CAACAgIAAxkBAAMjZ1QqHdXAmshyeBKB8VsNadUufMIAAvEAA5i_gA0rH5f5RLvJYTYE',
    'CAACAgIAAxkBAAMlZ1QqH6DnaSksrnn6TOKbCwp9NOEAAvkAA5i_gA2sCdXUlgobTjYE',
    'CAACAgIAAxkBAAMnZ1QqIQ3ajtURcHqgpUIsUz7215wAAv8AA5i_gA2a3Ycbg73cSDYE'
]

@bot.message_handler(content_types=['sticker'])
def handler_sticker(message):
    id = message.sticker.file_id
    em = message.sticker.emoji
    text = f"ІД наліпки = ({id}). Емоджі:({em}) "
    bot.reply_to(message, text)

@bot.message_handler(commands=['f'])
def handler_f(message):
    current_path_app = os.path.abspath(__file__)
    current_path = os.path.dirname(current_path_app)
    my_file = os.path.join(current_path, 'sticker', 'dog.webm')

    with open(my_file, 'rb') as sticker:
        bot.send_sticker(message.chat.id, sticker)


# ------ TEXT
@bot.message_handler(content_types=['text'])
def is_text(message):
    if message.text == 'a':
        bot.send_sticker(message.chat.id, sticker_list[0])
        return True
    elif message.text == 'b':
        bot.send_sticker(message.chat.id, sticker_list[1])
        return True
    elif message.text == 'c':
        bot.send_sticker(message.chat.id, sticker_list[2])
        return True
    elif message.text == 'd':
        bot.send_sticker(message.chat.id, sticker_list[3])
        return True
    elif message.text == 'u':
        bot.send_sticker(message.chat.id, sticker_list[4])
        return True

    bot.send_message(message.chat.id, 'OK!')

if __name__ == '__main__':
    bot.infinity_polling()
