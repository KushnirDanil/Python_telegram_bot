import telebot
import re

token = '7991465200:AAF-y2rC0pO6Qqhak89IeKrG8TbX2vp8V7c'
bot = telebot.TeleBot(token)

def is_integer(string):
    return string.isdigit()


def is_int(value):
    try:
        int(value)
        return True
    finally:
        return False


def is_float(string):
    try:
        float(string)
        return True
    except ValueError:
        return False


def is_number(string):
    return bool(re.match(r'^[-+]?\d*\.?\d+$', string))


@bot.message_handler(content_types=['text'])
def say_bot(message):

    if is_int(message.text):                 # Число
        with open('f1.txt', 'a') as file:
            file.write(message.text + '\n')
    else:                                   # Текст
        with open('f2.txt', 'a') as file:
            file.write(message.text + '\n')

    bot.send_message(message.chat.id, "ok!")

if __name__ == '__main__':
    bot.polling()

# Робота з файлами
import os
import random

# Завдання 1
# file_name = 'f1.txt'
# file = open(file_name, mode='w')
#
# try:
#     for n in range(0, 10):
#         file.write("Text: {num} {nl}".format(num=n, nl='\n'))
#         # file.write('Text: {} {}'.format(n, '\n'))
#
# finally:
#     file.close()


# Завдання 2
# file_name = 'f2.txt'
# with open(file_name, 'w') as file:
#     for n in range(0, 100):
#         file.write(str(random.randint(1, 1000)) + '\n')


# зчитування з файла
# with open('f1.txt', 'r') as file:
#     content = file.read()
#     print(content)

# with open('f1.txt', 'r') as file:
#     line = file.readline()
#     while line:
#         print(line)
#         # ... наш код
#         line = file.readline()

# with open('f1.txt', 'wt') as file:
#     for i in range(0, 10):
#         file.write(str(i) + '\n')


# Завдання 3
# with open("f2.txt", "w", encoding="utf-8") as file:
#     file.write(str(random.randint(0, 100)))
# with open("f2.txt", "r", encoding="utf-8") as file:
#     r = file.read()
#     print(r)
#
# with open('f2.txt', 'rb') as f:
#     byte = f.read(1)
#     while byte:
#         binary_representation = bin(byte[0])[2:].zfill(8)
#         print(binary_representation)
#         byte = f.read(1)

# with open('f3.bin', 'wb') as file:      # ASCII - Hex
#     file.write(b'\x50\x79\x74\x68\x6F\x6E\x21')
#
# # Читання бінарних даних
# with open('f3.bin', 'rb') as file:
#     binary_content = file.read()
#     print(binary_content)

