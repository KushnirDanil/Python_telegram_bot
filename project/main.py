from werkzeug.serving import make_ssl_devcert

import config as c
from SQLiteManeger import SQLNote
import telebot
import time
import threading
import sqlite3

bot = telebot.TeleBot(c.BOT_TOKEN)

# === SQLITE =====================================
# db = sqlite3.connect('notebook.db')
# cur = db.cursor()
#
# cur.execute('''CREATE TABLE IF NOT EXISTS users (
#         id INTEGER PRIMARY KEY,
#         chat_id INTEGER NOT NULL,
#         name TEXT DEFAULT 'Unknown',
#        email TEXT DEFAULT '',
#        deleted INTEGER DEFAULT 0
#     )''')
# db.commit()
#
# cur.execute('''CREATE TABLE IF NOT EXISTS notes (
#         id INTEGER PRIMARY KEY AUTOINCREMENT,
#         user_id INTEGER NOT NULL,
#         title TEXT NOT NULL,
#         content TEXT DEFAULT '',
#         notification DATETIME DEFAULT CURRENT_TIMESTAMP,
#         is_send INTEGER DEFAULT 0,
#         deleted INTEGER DEFAULT 0
#     )''')
# db.commit()
#
# === FUNCTIONS ==================================
def get_db_cursor():
    return SQLNote(c.DB_NAME)

def send_text_message():
    while True:
        # код ........
        bot.send_message('1875609992', 'Щось спрацювало')
        time.sleep(10)

def bot_add_title(message):
    # TODO: add note ................

    bot.send_message(message.chat.id, 'Нотатку додано!')

# === MESSAGE-HANDLERS ============================
# start - Підписатися
# add - Додатки
# edit - редагувати
# del - видалити
# all - покзати усі нотатки
# help - вивести підказки
# end - відписатися
@bot.message_handler(commands=['start', 'add', 'edit', 'del', 'help', 'end'])
def bot_commands(message):
    if '/start' == message.text:
        bot_start()
    elif '/add' == message.text:
        bot.send_message(message.chat.id, 'Введіть нотатку:')
        bot.register_next_step_handler(message, bot_add_title)
    elif '/edit' == message.text:
        pass

@bot.message_handler(commands=['start'])
def bot_start(message):
    print(message)
    with get_db_cursor() as cur:
        cur.execute("SELECT chat_id FROM users WHERE chat_id='%d'" % message.chat.id)
        row = cur.fetchone()

        if not row:
            chat_id = message.chat.id
            name = message.from_user.username
            cur.execute(f"INSERT INTO users (chat_id, name) VALUES ('{chat_id}', '{name}')")
            bot.send_message(message.chat.id, f'Користувача[{name}] Додано!')
        else:
            bot.send_message(message.chat.id, 'Ви вже підписалися на цього бота')

if __name__ == '__main__':
    # thread = threading.Thread(target=send_text_message)
    # thread.start()
    bot.infinity_polling()

