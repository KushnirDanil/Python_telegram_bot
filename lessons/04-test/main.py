import telebot
from telebot import types

token = '7991465200:AAF-y2rC0pO6Qqhak89IeKrG8TbX2vp8V7c'
bot = telebot.TeleBot(token)


# ---COMMANDS ---

@bot.message_handler(commands=['open']) # /open
def handler_open(message):
    # ...
    bot.send_message(message.chat.id, 'Відкрити двері')


@bot.message_handler(commands=['close']) # /close
def handler_close(message):
    # ...
    bot.send_message(message.chat.id, 'Закрити двері')

@bot.message_handler(commands=['start', 'stop', 'speed']) # /start, /stop, /speed
def handler_run_car(message):
    car = 'Стоїть'

    if message.text == '/start':
        car = 'Починаємо рух'
    elif message.text == '/stop':
        car = 'Зупинитися'
    elif message.text == '/speed':
        car = 'Змінити швидкість'


    bot.send_message(message.chat.id, car)


# 1. Додати клавіатуру
@bot.message_handler(commands=['pizza'])
def handler_pizza(message):
    keyboard = types.ReplyKeyboardMarkup(one_time_keyboard=True)
    btn1 = types.KeyboardButton(text='Папероні')
    btn2 = types.KeyboardButton(text='4 сира')
    btn3 = types.KeyboardButton(text='Діабло')
    keyboard.add( btn1, btn2, btn3 )

    mes = bot.send_message(message.chat.id,  'Виберіть піцу', reply_markup=keyboard)
    bot.register_next_step_handler(mes, pizza_order)


@bot.message_handler(commands=['drink'])
def handler_drinks(message):
    keyboard = types.ReplyKeyboardMarkup(one_time_keyboard=True)
    btn1 = types.KeyboardButton(text='Пепсі')
    btn2 = types.KeyboardButton(text='Квас')
    btn3 = types.KeyboardButton(text='Фреш')
    keyboard.add( btn1, btn2, btn3 )

    bot.send_message(message.chat.id,  'Виберіть напій', reply_markup=keyboard)


@bot.message_handler(func=lambda message: message.text == 'Пепсі')
def drinks_pepsi(message):
    bot.send_message(message.chat.id, 'Замовлено:' + message.text)

@bot.message_handler(func=lambda message: message.text == 'Фанта')
def drinks_fanta(message):
    bot.send_message(message.chat.id, 'Замовлено:' + message.text)

@bot.message_handler(func=lambda message: message.text == 'Фреш')
def drinks_fresh(message):
    bot.send_message(message.chat.id, 'Замовлено:' + message.text)

@bot.message_handler(commands=['ik'])
def inline_keyboard(message):
    inline_keyboard = types.InlineKeyboardMarkup()
    b1 = types.InlineKeyboardButton('Кнопка 1', callback_data='b1')
    b2 = types.InlineKeyboardButton('Кнопка 2', callback_data='b2')
    inline_keyboard.add(b1, b2)

    bot.send_message(message.chat.id, 'Зробіть вибір:', reply_markup=inline_keyboard)

@bot.callback_query_handler()
def f_b1(cl):
    if cl.data == 'b1':
        bot.send_message(cl.message.chat.id, 'Right choice(Правильний вибір)')
    elif cl.data == 'b2':
        bot.send_message(cl.message.chat.id, 'Not right choice(Не правильний вибір)')


# ---TEXT---

@bot.message_handler(content_types=['text'])
def test_text(message):
    print(message)

    msg = message.text + ' - this is a text message(це текстове повідомлення)'
    bot.send_message(message.chat.id, msg)

# --- FUNCTION ---
def pizza_order(message):
    if message.text == 'Папероні':
        pn = 1232
    elif message.text == '4 сира':
        pn = 11111
    elif message.text == 'Діабло':
        pn = 123
    bot.send_message(message.chat.id, f'Ваше замовлення піци: "{message.text}" прийнято! №{pn}')

if __name__ == '__main__':
    bot.infinity_polling()
