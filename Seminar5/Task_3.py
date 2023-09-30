# 4. Создайте функцию генератор чисел Фибоначчи
# https://ru.wikipedia.org/wiki/%D0%A7%D0%B8%D1%81%D0%BB%D0%B0_%D0%A4%D0%B8%D0%B1%D0%BE%D0%BD%D0%B0%D1%87%D1%87%D0%B8

def fibonacci(num: int):
    """
    Генерирует первые 'num' чисел последовательности Фибоначчи
    :param num: Количество чисел для генерации
    :return: ??? применимо ли для функции-генератора
    """
    first, second = 1, 1
    for _ in range(num):
        yield first
        first, second = second, first + second


fib_iter = fibonacci(10)
print(next(fib_iter))
print(next(fib_iter))
print(next(fib_iter))
print(next(fib_iter))
print(next(fib_iter))
print(next(fib_iter))
print(next(fib_iter))
print(next(fib_iter))
print(next(fib_iter))
print(next(fib_iter))

print(next(fib_iter)) # Показывает остановку итерации
