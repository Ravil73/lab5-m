import os
import csv


def read_csv_file(list):
    """
    Считывает элементы в data.csv и записывает все данные в лист data
    :param list лист объектов
    """
    with open("data.csv", "r") as cf:
        # csv.DictReader() - читает CSV файл как список словарей.
        file = csv.DictReader(cf, delimiter=";")
        for way in file:
            # append() - вставляет в конец исходного списка значение аргумента.
            list.append(way)
    print("Данные считаны успешно")


def count_file_in_directory(way_to_directory):
    """
    Подсчитывает кол-во файлов в пути, который задал пользователь
    :param way_to_directory путь до директории
    :return count кол-во файлов
    :return 0 если неверный путь
    """
    # "try - except" - для обработки исключений
    # "listdir()" - получение списка файлов в дириктории(только названия)
    # "os.path.isfile()" - для проверки того, является ли указанный путь существующим обычным файлом или нет
    # "os.path.join()" - правильно соединяет компоненты пути файловой системы, ставит "/"
    try:
        return len(
            [name for name in os.listdir(way_to_directory) if os.path.isfile(os.path.join(way_to_directory, name))])
    except:
        print("Неверный путь")
        return 0


def change_csv(list):
    """
    Изменяет данные в списке, который получили из data.csv
    :param list лист
    """
    STR = int(input("Строка для редактирования: "))
    k = input("Введите ключ, который надо поменять: ")
    v = input("Поменять на: ")
    if STR >= 0:
        list[STR][k] = v
        print("Успешно изменено")
    else:
        print("Строка не может быть отрицательной")


def sort_csv_list(list):
    """
    Сортирует массив по определённому ключу
    :param list лист
    """
    key = input("Сортировать по ключу: ")
    try:
        list.sort(key=lambda k: k[key])
        print("Сортировка прошла успешно")
    except:
        print("Такого ключа не существует")


def write_csv(list):
    """
    Перезаписывает файл data.csv на то, что было сохранено в list
    :param list массив
    """
    names = ['#', 'date_time_on', 'date_time_of', 'passing_cars', 'cars_waiting']
    with open("data.csv", "w") as csvfile:
        wrt = csv.DictWriter(csvfile, delimiter=";", fieldnames=names, lineterminator="\r")
        wrt.writeheader()
        for STR in list:
            wrt.writerow(STR)
    print("Данные успешно записаны в файл")


def print_specific_list(list):
    """
    Выводит только те строки, где количество машин в ожидании больше 100
    :param list лист
    """
    try:
        print_list(STR for STR in list if int(STR["cars_waiting"]) > 100)
    except:
        return 0


def print_list(list):
    """
    Выводит весь массив(словарь) в консоль
    :param list лист
    """
    for STR in list:
        print(STR)


def print_all_function():
    """
    Вывод на экран всех функций прогрыммы
    """
    print("1)Количество файлов в директории")
    print("2)Считать информацию из файла data.csv")
    print("3)Редактировать файл data.csv")
    print("4)Сортировать по ключу")
    print("5)Записать изменения в файл data.csv")
    print("6)Выборка по количеству ожидающих машин")
    print("7)Показать словарь")
    print("8)Показать функции программы")


def main():
    """
    Главная функция, в которой находятся основные функции программы
    """
    Dictionary = []
    print_all_function()
    while True:
        n = input("Выберите функцию: ")
        if n == '1':
            # "format()" - форматирует значение переменной для вывода на печать.
            # В данном случае добавляет количество файлов в директории
            print("Количество файлов: {}".format(count_file_in_directory(input("Введите путь: "))))
        elif n == '2':
            read_csv_file(Dictionary)
        elif n == '3':
            change_csv(Dictionary)
        elif n == '4':
            sort_csv_list(Dictionary)
        elif n == '5':
            write_csv(Dictionary)
        elif n == '6':
            print_specific_list(Dictionary)
        elif n == '7':
            print_list(Dictionary)
        elif n == '8':
            print_all_function()
        else:
            break


if __name__ == '__main__':
    main()
