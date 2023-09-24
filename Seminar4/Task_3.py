# 3. Возьмите задачу о банкомате из семинара 2. Разбейте её на отдельные операции — функции.
# Дополнительно сохраняйте все операции поступления и снятия средств в список.

# P.s.: на самом деле прям на семинаре уже сделали все через функции, так что здесь я просто
# добавил docstring + функционал записи операций в список

from datetime import datetime # для красоты добавим в историю операций текущие дату-время
__OPERATION_LIST__ = [] # глобальная переменная для хранения истории операций


def fill(money: int) -> int:
    """
    Функция пополнения счета на сумму, кратную 50 у.е.
    В конце добавляет факт выполнения операции в историю операций
    :param money: деньги на счету
    :return: сумма на счете после пополнения
    """
    while True:
        money_to_fill = int(input('Какую сумму (кратную 50 у.е.) вы хотите внести: '))
        if money_to_fill % 50 != 0:
            print('Введите сумму, кратную 50.')
        else:
            break

    __OPERATION_LIST__.append(f'{datetime.now()}: Пополнение наличных на {money_to_fill} у.е.')

    return money + money_to_fill


def get_money(money: int) -> int:
    """
    Функция снятия наличных, кратных 50 у.е. При снятии дополнительно забирает со счета процент для банка.
    Проверяет допустимость снятия (сумма для снятия вместе с процентами не больше остатка на счете).
    В конце добавляет операцию в историю операций.
    :param money: деньги на счету
    :return: текущий остаток на счету после снятия наличных
    """
    while True:
        money_to_take = int(input('Какую сумму (кратную 50 у.е.) вы хотите снять: '))
        percent = money_to_take * 0.015
        if percent < 30:
            money_with_percent = money_to_take + 30
        elif percent > 600:
            money_with_percent = money_to_take + 600
        else:
            money_with_percent = money_to_take + percent

        if money_to_take % 50 != 0:
            print('Введите значение, кратное 50.')
        elif money_with_percent > money:
            print('Недостаточно средств. Введите меньшую сумму.')
        else:
            break

    __OPERATION_LIST__.append(f'{datetime.now()}: Снятие {money_with_percent} у.е. (с учетом процента от банка) ')

    return money - money_with_percent


def you_wont_be_rich(money: int) -> int:
    """
    Кошмар любого клиента. Отбирает 10% при любой операции, если на счету более 5_000_000 у.е.
    :param money: деньги на счету
    :return: деньги на счету с учетом снятой комиссии
    """
    if money > 5_000_000:
        money *= 0.9
        __OPERATION_LIST__.append(f'{datetime.now()}: Снятие процента, так как у вас слишком много денег.')
    return money


def check_counter(counter: int, money: int) -> tuple:
    """
    Проверяем и увеличиваем на 1 количество операций, чтобы за каждую 3-ю начислить клиенту бонус.
    При достижении 3-х операций увеличиваем счет на 3%.
    :param counter: количество операций
    :param money: сумма на счету
    :return: количество операций и деньги на счету
    """
    counter += 1
    if counter == 3:
        money *= 1.03
        counter = 0
    __OPERATION_LIST__.append(f'{datetime.now()}: Проверка количества операций. У вас {3 - counter} операций до бонуса.')
    return counter, money


def check_operation_history():
    print(*__OPERATION_LIST__, sep='\n')


def main():
    """
    Основная логика. Взаимодействие с клиентом.
    Вызов функции снятия наличных и/или пополнения баланса, выход из программы.
    :return:
    """
    money = 0
    counter = 0
    while True:
        print('1. Пополнить счет.')
        print('2. Снять наличные.')
        print('3. Посмотреть историю операций.')
        print('4. Выйти.')
        while True:
            user_choice = int(input('Выберите номер операции: '))
            if user_choice not in [1, 2, 3, 4]:
                print('Неверный ввод, попробуйте еще раз.')
                money = you_wont_be_rich(money)
                print(money)
            else:
                break

        if user_choice == 1:
            money = you_wont_be_rich(money)
            money = fill(money)
            counter, money = check_counter(counter, money)
            print(money)
        elif user_choice == 2:
            money = you_wont_be_rich(money)
            money = get_money(money)
            counter, money = check_counter(counter, money)
            print(money)
        elif user_choice == 3:
            money = you_wont_be_rich(money)
            counter, money = check_counter(counter, money)
            check_operation_history()
        else:
            money = you_wont_be_rich(money)
            print('До свидания!')
            print(money)
            return


if __name__ == '__main__':
    main()