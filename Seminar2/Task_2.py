# Напишите программу, которая принимает две строки вида “a/b” - дробь с числителем и знаменателем.
# Программа должна возвращать сумму и произведение* дробей. Для проверки своего кода используйте модуль fractions

from fractions import Fraction

# Верификация ввода от пользователя.
# По идее при правильном вводе после split('/') должны остаться два числа в строковом виде,
# которые спокойно кастуются в int(). При неправильном вводе в int не кастуется -> ловится ошибка ValueError.
while True:
    try:
        first_frac = [int(i) for i in input('Введите дробь в виде "a/b", где "a" и "b" - целые числа: ').split('/')]
        second_frac = [int(i) for i in input('Введите дробь в виде "a/b", где "a" и "b" - целые числа: ').split('/')]
        break
    except ValueError:
        print('Неправильный ввод. Попробуйте еще раз, следуйте подсказкам.')


def fraction_sum(frac_1: list, frac_2: list) -> list:
    """
    Функция нахождения суммы дробей.
    :param frac_1: Первая дробь: список двух чисел в котором первое - делимое, второе - делитель.
    :param frac_2: Вторая дробь: список двух чисел в котором первое - делимое, второе - делитель.
    :return: Результат сложения в виде списка из двух чисел, в котором первое - делимое, второе - делитель.
    """
    return [frac_1[0] * frac_2[1] + frac_2[0] * frac_1[1], frac_1[1] * frac_2[1]]


def fraction_prod(frac_1: list, frac_2: list) -> list:
    """
    Функция произведения дробей.
    :param frac_1: Первая дробь: список двух чисел в котором первое - делимое, второе - делитель.
    :param frac_2: Вторая дробь: список двух чисел в котором первое - делимое, второе - делитель.
    :return: Результат произведения в виде списка в котором первое - делимое, второе - делитель.
    """
    return [frac_1[0] * frac_2[0], frac_1[1] * frac_2[1]]


def greater_general_delimiter(num_1: int, num_2: int) -> int:
    """
    Функция для нахождения наибольшего общего делителя (НОД).
    Требуется для сокращения результата суммы (произведения) дробей.
    :param num_1: Делимое дроби
    :param num_2: Делитель дроби
    :return: НОД чисел дроби.
    """
    result = 1
    if num_1 > num_2:
        num_1, num_2 = num_2, num_1
    for i in range(1, num_1 + 1):
        if num_1 % i == 0 and num_2 % i == 0:
            result = i
    return result


# Проверка работы произведения дробей
print()
result_prod = fraction_prod(first_frac, second_frac)
prod_delimiter = greater_general_delimiter(result_prod[0], result_prod[1])
print(f"Произведение дробей: {int(result_prod[0] / prod_delimiter)}/{int(result_prod[1] / prod_delimiter)}")
print(f"Проверка произведения модулем Fraction: "
      f"{Fraction(first_frac[0], first_frac[1]) * Fraction(second_frac[0], second_frac[1])}")

# Проверка работы суммы дробей
print()
result_sum = fraction_sum(first_frac, second_frac)
sum_delimiter = greater_general_delimiter(result_sum[0], result_sum[1])
print(f"Сумма дробей: {int(result_sum[0] / sum_delimiter)}/{int(result_sum[1] / sum_delimiter)}")
print(f"Проверка суммы модулем Fraction: "
      f"{Fraction(first_frac[0], first_frac[1]) + Fraction(second_frac[0], second_frac[1])}")
