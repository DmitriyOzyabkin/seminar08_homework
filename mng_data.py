import mng_file

def name_data():
    name = input("Введите имя:")
    print("Принято")
    return name


def surname_data():
    surname = input("Введите фамилию:")
    print("Принято")
    return surname


def phone_data():
    phone = input("Введите номер тедефона:")
    print("Принято")
    return phone


def address_data():
    address = input("Введите адрес:")
    print("Принято")
    return address

def continue_request():
    command = input("Продолжить? (Да/Нет): ").lower()
    while command not in ['да', 'нет']:
        print("Ответ не ясен")
        command = input("Продолжить? (Да/Нет): ").lower()
    if command == 'да':
        return True
    else:
        return False


def find_first_data(request):
    data = mng_file.create_first_data_dict()
    result = {}
    index = 1
    for entry in data.values():
        value = [note.lower() for note in entry]
        if request.lower() in value:
            result[index] = entry
            index += 1
    return result


def find_second_data(request):
    data = mng_file.create_second_data_dict()
    result = {}
    index = 1
    for entry in data.values():
        value = [note.lower() for note in entry]
        if request.lower() in value:
            result[index] = entry
            index += 1
    return result


