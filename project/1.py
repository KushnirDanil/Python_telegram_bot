# def decorator(func):
#     def wrap():
#         print('start')
#         func()
#         print('end')
#
#     return wrap
#
#
# @decorator
# def con_pri():
#     print('наша функція')
#
#
# con_pri()

def decorator(func):
    def wrap(*args, **kwargs):
        print('start')
        func(*args, **kwargs)
        print('end')
    return wrap


@decorator
def con_pri(text=''):
    print('наша функція', text)


con_pri('additional')
