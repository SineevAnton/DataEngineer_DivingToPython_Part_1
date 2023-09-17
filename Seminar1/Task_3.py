# Программа загадывает число от 0 до 1000. Необходимо угадать число за 10 попыток.
# Программа должна подсказывать “больше” или “меньше” после каждой попытки.
# Для генерации случайного числа используйте код:
# from random import randint
# num = randint(LOWER_LIMIT, UPPER_LIMIT)

# Блок импортов
from random import randint

# Блок методов


def game_start(computer_number: int):
    """

    :param number:
    :return:
    """
    print("Игра: 'Угадай число'.\n Компьютер загадал число от 0 до 1000. У вас есть 10 попыток, чтобы угадать"
          " загаданное число. Удачи ^_^")

    attempts = 3
    while True:
        user_number = user_dialog()
        if attempts == 0:
            print("У вас не осталось попыток, вы проиграли.")
            print(f"Компьютер загадал {computer_number}")
            break
        elif user_number == computer_number:
            print("Вы угадали число! Поздравляю!")
            print(f"Компьютер действительно загадал {computer_number}")
            break
        elif user_number > computer_number:
            print("Неверно. Загаданное число меньше.")
            print(f"У вас осталось {attempts} попыток(-ки)")
            attempts -= 1
        else:
            print("Неверно. Загаданное число больше.")
            print(f"У вас осталось {attempts} попыток(-ки)")
            attempts -= 1



def user_dialog() -> int:
    """
    Method to get the guess number from user and check if it belongs to allowed range
    :return: 'int' variable "number"
    """
    while True:
        number = int(input("Введите число от 0 до 1000: "))
        if not 0 <= number <= 1000:
            print("Неверный ввод!")
        else:
            break

    return number


game_start(randint(0, 1001))