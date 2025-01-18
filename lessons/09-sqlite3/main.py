import config
import telebot
import time
import threading
import sqlite3

bot = telebot.TeleBot(config.BOT_TOKEN)

# === SQLITE =====================================
db = sqlite3.connect('notebook.db')
cur = db.cursor()

# cur.execute('''CREATE TABLE user (
#         id INTEGER PRIMARY KEY,
#         chat_id INTEGER NOT NULL,
#         name TEXT DEFAULT 'Unknown',
#         email TEXT DEFAULT '',
#         deleted INTEGER DEFAULT 0
#     )''')
# db.commit()


# === FUNCTIONS ==================================
def send_text_message():
    while True:
        # код ......
        bot.send_message('1875609992', 'Щось спрацювало')
        time.sleep(10)

# === MESSAGE-HANDLERS ============================
@bot.message_handler(commands=['start'])
def bot_start(message):

    # TODO: КОНТЕКСТ ........
    cur.execute("SELECT chat_id FROM user")
    row = cur.fetchone()
    if not row:
        chat_id = message.chat.id
        name = message.from_user.username
        cur.execute(f" INSERT INTO user (chat_id, name,) VALUES ({chat_id}, {name})")
        db.commit()

    bot.send_message(message.chat.id, f'Користувача[{name}] Додано!')

@bot.message_handler(content_types=['text'])
def text_massage(message):
    bot.send_message(message.chat.id, 'Працює!')

if __name__ == '__main__':
    # thread = threading.Thread(target=send_text_message)
    # thread.start()
    bot.infinity_polling()

