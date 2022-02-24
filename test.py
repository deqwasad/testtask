from random import randint


def sorting(sorting_i, sorting_array_secondary, sorting_array_final):  # сортировка размера, с которым проводится работа
    if sorting_i % 2 == 1:
        array_secondary = sorted(sorting_array_secondary)
    else:
        array_secondary = sorted(sorting_array_secondary, reverse=True)
    sorting_array_final.append(array_secondary)
    return sorting_array_final


def filling(number):  # заполнение массива
    array_final = []  # финальный массив
    array_size = []  # массив размеров полученных массивов
    counter = 0
    for i in range(number):
        size_of_array = randint(1, number)  # размер массива, с которым проводится работа
        while counter < len(array_size):
            if size_of_array == array_size[counter]:
                counter = 0
                size_of_array = randint(1, number)
            else:
                counter += 1
        array_size.append(size_of_array)
        counter = 0
        array_secondary = []
        for j in range(size_of_array):
            element = randint(1, number)
            array_secondary.append(element)
        array_final = sorting(i, array_secondary, array_final)
    return array_final


input_number = int(input())
answer = filling(input_number)

