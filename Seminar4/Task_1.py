# 1. Напишите функцию для транспонирования матрицы

def create_matrix(rows: int = 4, cols: int = 5) -> list[list]:
    """
    Функция для генерации матрицы, заполненной случайными величинами.
    :param rows: Число строк сгенерированной матрицы (по дефолту - 4).
    :param cols: Число колонок сгенерированной матрицы (по дефолту - 5).
    :return: сгенерированную матрицу.
    """
    from random import randint

    result = [[randint(1,10) for _ in range(cols)] for _ in range(rows)]

    return result


def transpose_matrix(matrix: list[list]) -> list[list]:
    """
    Функция, которая транспонирует переданную матрицу.
    :param matrix: Матрица для транспонирования
    :return: Матрица - результат транспонирования.
    """
    result = [[matrix[r][c] for r in range(len(matrix))] for c in range(len(matrix[0]))]

    return result


def print_matrix(matrix: list[list], message: str = 'Матрица:') -> None:
    """
    Функция вывода матрицы в консоль.
    :param matrix: Матрица для вывода.
    :param message: Уточняющее сообщение.
    :return: None
    """
    print(message)
    # for row in matrix:
    #     print(*row)

    # Выше быстрый вывод, ниже - более красивый (добавлена табуляция между элементами для выравнивания вывода)

    for r in range(len(matrix)):
        print()
        for c in range(len(matrix[0])):
            print(matrix[r][c], end='\t')
    print('\n\n')


if __name__ == '__main__':
    original_matrix = create_matrix(4, 5)
    print_matrix(original_matrix, 'Исходная матрица:')
    transposed_matrix = transpose_matrix(original_matrix)
    print_matrix(transposed_matrix, 'Транспонированная матрица:')