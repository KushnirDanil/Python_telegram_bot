# import random
# filename = 'f1.txt'
#
# # #Запис
# with open(filename, 'w') as f:
#     f.write('New text')
#
# # Зчитування
# with open(filename, 'r') as f:
#     text = f.read()
#     print(text)
#
# f = open(filename, 'r')
# try:
#     text = f.read()
#     print(text)
# finally:
#     f.close()
#
# with open(filename, 'w') as file:
#     for n in range(0,10):
#         file.write(str(random.randint(-10,10)) + '\n')
#
# with open(filename, 'r') as file:
#     number = file.readline()
#     while number:
#         print(number)
#         number = file.readline()
#
# filename = 'f3.txt'
# with open (filename, 'w', encoding='utf-8') as  file:
#     file.write('Text utf-8.')
#
# filename = 'f3.txt'
# with open (filename, 'r', encoding='utf-8') as  file:
#     print(file.read())
#
# filename = 'bq.txt'
# with open(filename, 'ab') as file:
#     file.write(b"\x4B\x4D\x4A\x3F")
#
# with open(filename, 'rb') as file:
#     content = file.readline()
#     print(content)