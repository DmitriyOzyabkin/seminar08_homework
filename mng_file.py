import mng_data

def input_data():
    name = mng_data.name_data()
    surname = mng_data.surname_data()
    phone = mng_data.phone_data()
    address = mng_data.address_data()
    var = int(input(f"""Выбирете формат данных

    1. Многострочный
        {name}
        {surname}
        {phone}
        {address}

    2. Однострочный {name};{surname};{phone};{address}\n
Ваш вариант?: """))

    while var != 1 and var != 2:
        print(f"""\nБудте внимательны, варианта {var} не существует. Повторите ввод:

    1. Многострочный формат
    2. Однострочный формат\n""")
        var = int(input())

    if var == 1:
        with open('data_first_var.csv', 'a', encoding='utf-8') as file:
            file.write(f"{name}\n{surname}\n{phone}\n{address}\n\n")

    elif var == 2:
        with open('data_second_var.csv', 'a', encoding='utf-8') as file:
            file.write(f"{name};{surname};{phone};{address}\n\n")

def create_first_data_dict():
    with open('data_first_var.csv', 'r', encoding='utf-8') as file:
        data_first = file.readlines()
        data_first_dict = {}
        key_number = 1
        j = 0
        for i in range(len(data_first)):
            if data_first[i] == '\n' or i == len(data_first) - 1:
                data_first_dict[key_number] = data_first[j:i]
                for elem in range(len(data_first_dict[key_number])):
                    data_first_dict[key_number][elem] = data_first_dict[key_number][elem][:-1]
                key_number += 1
                j = i+1
        return data_first_dict


def create_second_data_dict():
    with open('data_second_var.csv', 'r', encoding='utf-8') as file:
        data_second = file.readlines()
        while '\n' in data_second:
            data_second.remove('\n')
        data_second_dict = {}
        key_number = 1
        for entry in data_second:
            data_second_dict[key_number] = entry.split(';')
            data_second_dict[key_number][3] = data_second_dict[key_number][3][:-1]
            key_number += 1
    return data_second_dict


def write_first_file(data_dict: dict):
    with open('data_first_var.csv', 'w', encoding='utf-8') as file:
        for entry in data_dict.values():
            for data in entry:
                file.write(f"{data}\n")
            file.write("\n")


def write_second_file(data_dict: dict):
    with open('data_second_var.csv', 'w', encoding='utf-8') as file:
        for entry in data_dict.values():
            file.write(';'.join(entry))
            file.write("\n\n")


def edit_first_data(entry_key: int, data_index: int, data_dict: dict, new_data):
    data_dict[entry_key][data_index] = new_data
    write_first_file(data_dict)
    return data_dict


def edit_second_data(entry_key: int, data_index: int, data_dict: dict, new_data):
    data_dict[entry_key][data_index] = new_data
    write_second_file(data_dict)
    return data_dict


def delete_first_data(key: int, data_dict: dict):
    del data_dict[key]
    write_first_file(data_dict)
    result_dict = create_first_data_dict()
    return result_dict


def delete_second_data(key: int, data_dict: dict):
    del data_dict[key]
    write_second_file(data_dict)
    result_dict = create_second_data_dict()
    return result_dict



def print_first_file(data_dict):

    for key_number in data_dict.keys():
        print(f"{key_number}: {data_dict[key_number][0]}"
              f"\n   {data_dict[key_number][1]}"
              f"\n   {data_dict[key_number][2]}"
              f"\n   {data_dict[key_number][3]}\n")


def print_second_file(data_dict):

    for key_number in data_dict.keys():
        print(f"{key_number}: {data_dict[key_number][0]} {data_dict[key_number][1]} {
              data_dict[key_number][2]} {data_dict[key_number][3]}\n")
        key_number += 1
