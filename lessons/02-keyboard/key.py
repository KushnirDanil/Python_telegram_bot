import telebot
from telebot import types
import os

token = "7991465200:AAF-y2rC0pO6Qqhak89IeKrG8TbX2vp8V7c"
bot = telebot.TeleBot(token)

list_sticker = ['CAACAgIAAxkBAAO3Z0iqLLOSpaCz8_EVHM7uWxrxLD4AAgUAA8A2TxP5al-agmtNdTYE']


# --- commands ----------------------------------------------------------------
@bot.message_handler(commands=['key'])
def key_function(message):
    keyboard = types.ReplyKeyboardMarkup(one_time_keyboard=True)
    button_1 = types.KeyboardButton(text='button 1')
    button_2 = types.KeyboardButton(text='button 2')
    keyboard.add(button_1, button_2)

    msg = bot.send_message(message.chat.id, message.text + 'Key!', reply_markup=keyboard)
    bot.register_next_step_handler(msg, bot_button_function)


# --- functions ---------------------------------------------------------------
def bot_button_function(message):
    if message.text == 'button 1':
        bot.send_message(message.chat.id, '1')
    elif message.text == 'button 2':
        bot.send_message(message.chat.id, '2')
    else:
        bot.send_message(message.chat.id, 'none')


if __name__ == '__main__':
    bot.infinity_polling()
