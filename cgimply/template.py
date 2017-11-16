"""
    Предоставление функционала шаблонизации
"""


def template(text, **kwargs):
    """
        Заполнение шаблона данными
    """
    return text.format(**kwargs)
