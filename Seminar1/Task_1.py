# Треугольник существует только тогда, когда сумма любых двух его сторон больше третьей.
# Дано a, b, c - стороны предполагаемого треугольника.
# Требуется сравнить длину каждого отрезка-стороны с суммой двух других.
# Если хотя бы в одном случае отрезок окажется больше суммы двух других,
# то треугольника с такими сторонами не существует.
# Отдельно сообщить является ли треугольник разносторонним, равнобедренным или равносторонним.


class Triangle:
    """
    Class for determining triangle, using lengths of it sides.
    """

    # attributes (properties):
    length_a = 5
    length_b = 5
    length_c = 5

    # methods (functions)

    def __init__(self, len_a, len_b, len_c):
        """
        Init magic method.
        :param len_a:
        :param len_b:
        :param len_c:
        """
        self.length_a = len_a
        self.length_b = len_b
        self.length_c = len_c
        self.validation()

    def set_sides_length(self, len_a, len_b, len_c):
        """

        :param len_a:
        :param len_b:
        :param len_c:
        :return:
        """
        self.length_a = len_a
        self.length_b = len_b
        self.length_c = len_c

    def get_sides_length(self):
        """

        :return:
        """
        return self.length_a, self.length_b, self.length_c

    def validation(self):
        sum_ab = self.length_a + self.length_b
        sum_bc = self.length_b + self.length_c
        sum_ac = self.length_a + self.length_c
        invalid_lengthes = self.length_a <= 0 or self.length_b <= 0 or self.length_c <= 0

        if self.length_a > sum_bc or self.length_b > sum_ac or self.length_c > sum_ab or invalid_lengthes:
            print("Треугольник с такими сторонами не может существовать! Объект будет уничтожен.")
            del self
        else:
            if self.length_a == self.length_b and self.length_b == self.length_c:
                print("Треугольник равносторонний.")
            elif self.length_a == self.length_b or self.length_b == self.length_c or self.length_a == self.length_c:
                print("Треугольник равнобедренный.")
            else:
                print("Самый обычный треугольник.")

    def __del__(self):
        print("Удаление экземпляра: " + str(self))


tr_1 = Triangle(0, 1, 2)
tr_2 = Triangle(1, 0, 2)
tr_3 = Triangle(1, 2, 0)
tr_3 = Triangle(3, 4, 5)
tr_3 = Triangle(5, 6, 5)
tr_3 = Triangle(6, 6, 6)

