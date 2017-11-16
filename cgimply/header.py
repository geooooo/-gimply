"""
    Модуль отправки заголовков ответа
"""


def header(name, value):
    """
        Отправка заголовка
    """
    print("{0}:{1}".format(name, value))


def headers(**kwargs):
    """
        Отправка нескольких заголовков
    """
    for name, value in kwargs:
        header(name, value)
    print()
