# Напишите программу, которая получает целое число и возвращает его шестнадцатеричное строковое представление.
# Функцию hex используйте для проверки своего результата.


class Number:

    __NUMBER_CONVERTER__ = {
        0: '0',
        1: '1',
        2: '2',
        3: '3',
        4: '4',
        5: '5',
        6: '6',
        7: '7',
        8: '8',
        9: '9',
        10: 'A',
        11: 'B',
        12: 'C',
        13: 'D',
        14: 'E',
        15: 'F',
    } # Конвертер чисел в определенную систему счисления
    __instance = None # Для теста Singleton

    def __new__(cls, *args, **kwargs):
        """
        Тест паттерна Singletone. Понимаю, что он тут не совсем уместен, однако...
        а) тест ради теста
        б) если код использовать в чем-то вроде калькулятора, то да - неуместно,
        а если делать какой-нибудь чистый конвертер, то, считаю, вполне имеет место быть
        :param args:
        :param kwargs:
        """
        if cls.__instance is None:
            cls.__instance = super().__new__(cls)
        return cls.__instance

    def __init__(self, value, base):
        """
        Инициализирует экземпояр класса, используя переданные значения value и base
        :param value: Число для конвертации
        :param base: Основание для конвертации
        """
        if self.verification(value, base):
            self.value = value
            self.base = base

    def verification(self, value, base):
        """
        Проверяет переданные в экземпляр значения
        :param value: Число для конвертации, должно быть целым.
        :param base: Основание для конвертации, должно быть целым в диапазоне от 2 до 16 (включая границы)
        :return: True, если данные корректны, иначе False
        """
        if not (isinstance(value, int) and isinstance(base, int) and (1 < base < 17)):
            print('Переданы некорректные параметры, экземпляр класса будет уничтожен.')
            del self
            print('Подсказка:\n- число должно быть целым;\n'
                  '- основание должно быть целым в диапазоне от 2 до 16, включительно.')
            return False
        else:
            return True

    def set_value(self, value):
        """
        Сеттер экземпляра класса
        :param value: Число для конвертации
        :return:
        """
        self.value = value

    def get_value(self):
        """
        Геттер экземпляра класса
        :return: Число, переданное в экземпляр для конвертации
        """
        return self.value

    def get_user_base_from_dec(self):
        """
        Конвертер числа в выбранную систему счисления
        :return: строковое представление числа, конвертированного в выбранную систему счисления
        """
        number = self.value

        converted_number = ''
        while number > 0:
            converted_number += self.__NUMBER_CONVERTER__[(number % self.base)]
            number //= self.base

        return converted_number[::-1]


# Две строки ниже чтобы пробежаться проверкой сразу по нескольким конвертациям
numbers_and_bases = [(77, 2), (77, 8), (77, 16)]
check_functions = {2: bin,
                   8: oct,
                   16: hex}

# Перебираем числа и основания из списка 'numbers_and_bases',
# передаем в экземпляр класса, проверяем встроеннымы функциями из словаря 'check_functions'
for element in numbers_and_bases:
    number = Number(element[0], element[1]) #
    print(f'Конвертированное число по основанию {element[1]}: {number.get_user_base_from_dec()}')
    print(f'Проверка встроенной функцией: {check_functions[element[1]](number.value)[2:]}')


# Ниже дефолтный вариант, без использования ООП и других усложнений.

# user_number = int(input('Введите число: '))
# base = int(input('Введите основание: '))
# check_number = user_number
#
# converted_number = ''
# while user_number > 0:
#     converted_number += number_converter[(user_number % base)]
#     user_number //= base
#
# print(converted_number[::-1])
# print(hex(check_number)[2:])