from mng_data import *
from mng_file import *


def interface():                                # Основное меню
    print("""\n\tОСНОВНОЕ МЕНЮ
    Что вы хотите сделать?:
    1. Внести новую запись
    2. Изменить существующую запись
    3. Найти запись
    4. Показать записи
    5. Удалить запись
    0. Выход\n""")

    command_main = int(input('Ваша команда: '))

    while command_main not in [1, 2, 3, 4, 5, 0]:
        print(f"""Будте внимательны, команды с номером {command_main} не существует.\nПовторите ввод команды:
    1. Внести новую запись
    2. Изменить существующую запись
    3. Найти запись
    4. Показать записи
    5. Удалить запись
    0. Выход\n""")
        command_main = int(input('Ваша команда: '))

    if command_main == 1:                   # Внесение новых записей
        input_data()
        print("Новая запись создана\n")
        if continue_request():
            interface()
        else:
            print('\nДосвидания!')

    elif command_main == 2:                 # Изменение в файлах
        print("""\nВ каком файле вы хотите внести изменения?\n
    1. Файл 1 (многострочные записи)
    2. Файл 2 (однострочные записи)
    0. Передумал. Выйти в главное меню""")

        command_edit = int(input("\nИзменить файл: "))

        while command_edit not in [1, 2, 0]:
            print("Такого файла нет. Повторите ввод\n")
            command_edit = int(input("\nИзменить файл: "))
        if command_edit == 1:
            current_dict = create_first_data_dict()
            print_first_file(current_dict)

            entery_key = int(
                input("Введите номер записи для редактирования: "))
            print("""\nЧто вы хотите изменить?\n
    1. Имя
    2. Фамилию
    3. Телефон
    4. Адрес\n""")

            data_index = int(input("\nИзменить: ")) - 1
            new_data = input("\nВведите новые данные: ")
            new_data_dict = edit_first_data(
                entery_key, data_index, current_dict, new_data)
            print_first_file(new_data_dict)
            print("\nИзменения сохранены\n")
            if continue_request():
                interface()
            else:
                print('Досвидания!\n')

        elif command_edit == 2:
            current_dict = create_second_data_dict()
            print_second_file(current_dict)
            entery_key = int(
                input("Введите номер записи для редактирования: "))
            print("""\nЧто вы хотите изменить?\n
    1. Имя
    2. Фамилию
    3. Телефон
    4. Адрес\n""")
            data_index = int(input("Изменить: ")) - 1
            new_data = input("\nВведите новые данные: ")
            new_data_dict = edit_second_data(
                entery_key, data_index, current_dict, new_data)
            print_second_file(new_data_dict)
            print("\nИзменения сохранены\n")
            if continue_request():
                interface()
            else:
                print('\nДосвидания!')

        if command_edit == 0:
            interface()

    elif command_main == 3:                 # Поиск записей
        print("""\nВ каком файле нужно выполнить поиск?\n
    1. Файл 1 (многострочные записи)
    2. Файл 2 (однострочные записи)
    0. Я передумал. Выход в главное меню\n""")
        command_find = int(input("\nПоиск в файле: "))
        while command_find not in [1, 2, 0]:
            print("Такого файла нет. Повторите ввод\n")
            command_delete = int(input("\nПоиск в файле: "))
        if command_find == 1:
            request = input("\nВведите данные для поиска: ")
            answer = find_first_data(request)
            if len(answer) == 0:
                print("\nДанные не обнаружены\n")
            else:
                print(f"\nОбнаружено {len(answer)} записей:\n")
                print_first_file(answer)

            if continue_request():
                interface()
            else:
                print('\nДосвидания!\n')

        elif command_find == 2:
            request = input("\nВведите данные для поиска: ")
            answer = find_second_data(request)
            if len(answer) == 0:
                print("\nДанные не обнаружены\n")
            else:
                print(f"\nОбнаружено {len(answer)} записей:\n")
                print_second_file(answer)

            if continue_request():
                interface()
            else:
                print('\nДосвидания!\n')

        elif command_find == 0:
            interface()

    elif command_main == 4:                 # Показать все
        print("""\nКакой файл вывести на экран?\n
    1. Файл 1 (многострочные записи)
    2. Файл 2 (однострочные записи)
    3. Оба файла
    0. Выход в главное меню\n""")
        command_print = int(input("\nВывести на экра вариант: "))
        if command_print == 1:
            print("\nВывожу данные 1 файла:\n")
            current_dict = create_first_data_dict()
            print_first_file(current_dict)

            if continue_request():
                interface()
            else:
                print('\nДосвидания!\n')

        elif command_print == 2:
            print("\nВывожу данные 2 файла:\n")
            current_dict = create_second_data_dict()
            print_second_file(current_dict)

            if continue_request():
                interface()
            else:
                print('\nДосвидания!\n')

        elif command_print == 3:
            print("\nВывожу данные из двух файлов:\n")
            print("Файл 1:\n")
            current_dict = create_first_data_dict()
            print_first_file(current_dict)
            print("Файл 2:\n")
            current_dict = create_second_data_dict()
            print_second_file(current_dict)

            if continue_request():
                interface()
            else:
                print('\nДосвидания!\n')

        elif command_print == 0:
            interface()

    elif command_main == 5:                 # Удаление записей
        print("""\nВ каком файле вы хотите удалить запись?\n
    1. Файл 1 (многострочные записи)
    2. Файл 2 (однострочные записи)
    0. Передумал. Выйти в главное меню""")

        command_delete = int(input("\nУдалить из файла: "))

        while command_delete not in [1, 2, 0]:
            print("Такого файла нет. Повторите ввод\n")
            command_delete = int(input("\nУдалить из файла: "))
        if command_delete == 1:
            current_dict = create_first_data_dict()
            print("\nФайл содержит следующие данные: \n")
            print_first_file(current_dict)

            entery_key = int(
                input("\nВведите номер записи для удаления: "))
            print("""\nВы действительно хотите удалить запись?
            Даные будут утеряны безвозвратно!!!!""")
            delete_request = input("\nУдалить (Да/Нет): ").lower()
            while delete_request not in ['да', 'нет']:
                print("\nВаш ответ не распознан.\n")
                delete_request = input("\nУдалить (Да/Нет): ").lower()
            if delete_request == "да":
                new_data_dict = delete_first_data(entery_key, current_dict)
                print_first_file(new_data_dict)
                print("\nДанные удалены\n")
                if continue_request():
                    interface()
                else:
                    print('Досвидания!\n')
            elif delete_request == "нет":
                interface()

        if command_delete == 2:
            current_dict = create_second_data_dict()
            print("\nФайл содержит следующие данные: \n")
            print_second_file(current_dict)

            entery_key = int(
                input("\nВведите номер записи для удаления: "))
            print("""\nВы действительно хотите удалить запись?
            Даные будут утеряны безвозвратно!!!!""")
            delete_request = input("\nУдалить (Да/Нет): ").lower()
            while delete_request not in ['да', 'нет']:
                print("\nВаш ответ не распознан.\n")
                delete_request = input("\nУдалить (Да/Нет): ").lower()
            if delete_request == "да":
                new_data_dict = delete_second_data(entery_key, current_dict)
                print_second_file(new_data_dict)
                print("\nДанные удалены\n")
                if continue_request():
                    interface()
                else:
                    print('Досвидания!\n')
            elif delete_request == "нет":
                interface()

        if command_delete == 0:
            interface()
    elif command_main == 0:                 # Выход
        print("\nДосвидания!")
