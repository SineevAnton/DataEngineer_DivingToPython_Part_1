# Создайте словарь со списком вещей для похода в качестве ключа и их массой в качестве значения.
# Определите какие вещи влезут в рюкзак передав его максимальную грузоподъёмность.
# Достаточно вернуть один допустимый вариант.
# *Верните все возможные варианты комплектации рюкзака.

things_to_hike = {
    "бутыль воды": 1,
    "веревка": 0.5,
    "палатка": 3,
    "котелок": 4,
    "консерва": 1.5,
}


def pack_a_backpack(backpack_limit, things, lastindex=0, lst=[]):
    """
    Функция, рекурсивно подсчитывающая возможную комплектацию рюкзака
    в зависимости от его грузоподъемности и весов переносимых предметов
    :param backpack_limit: грузоподъемность рюкзака
    :param things: словарь с вещами для закрузки (ключи) и их весами (значения)
    :param lastindex: вспомогательная переменная для рекурсивного вызова
    :param lst: список, в который запишутся веса переносимых предметов, для дальнейшего формирования вывода
    :return: nothing
    """
    weights = list(things.values())
    if backpack_limit == 0:
        for thing, weight in things.items():
            if weight in lst:
                print(f"{lst.count(weight)} - {thing}", end="; ")
        print()
    else:
        for i in range(lastindex, len(weights)):
            if weights[i] <= backpack_limit:
                pack_a_backpack(backpack_limit - weights[i], things, i, lst + [weights[i]])


pack_a_backpack(6, things_to_hike)