def get_name():
    number = input('Введите номер документа:')
    for data in documents:
        if data.get("number") == number:
            print('Владелец документа:')
            return data.get('name')
    return 'Владелец документа не найден.'


def get_shelf():
    number = input('Введите номер документа:')
    for key in directories:
        if number in directories.get(key):
            print('Документ хранится на полке:')
            return key
    return 'Документ не найден.'

documents = [
    {"type": "passport", "number": "2207 876234", "name": "Василий Гупкин"},
    {"type": "invoice", "number": "11-2", "name": "Геннадий Покемонов"},
    {"type": "insurance", "number": "10006", "name": "Аристарх Павлов"}
]

directories = {
    '1': ['2207 876234', '11-2'],
    '2': ['10006'],
    '3': []
}

while True:
    print('Возможные команды: p, s')
    comand = input('Введите название команды ')

    if comand == 'p':
        print(get_name())

    elif comand == 's':
        print(get_shelf())