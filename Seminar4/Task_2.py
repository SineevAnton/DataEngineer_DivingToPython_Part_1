# 2. Напишите функцию принимающую на вход только ключевые параметры и возвращающую словарь,
# где ключ — значение переданного аргумента, а значение — имя аргумента.
# Если ключ не хешируем, используйте его строковое представление.

def make_dict(**kwargs):
    """
    Функция создает словарь, в котором ключи - значения переданных переменных
    (в случае если значение не является хэшируемым объектом - оно заменяется на свое
    строковое представление), а, собственно, значения - ключи.
    :param kwargs: Передаваемые именованные аргументы
    :return: словарь, сформированный согласно условию
    """
    import typing

    result = {}

    for key, value in kwargs.items():
        if isinstance(value, typing.Hashable):
            result[value] = key
        else:
            result[str(value)] = key

    return result


if __name__ == '__main__':
    my_dict = make_dict(n=2, s="str", t=(1, 2), b=True, d={1: "one", 2: "two"}, f=4.56, l=[1, 2, 3])
    print(my_dict)