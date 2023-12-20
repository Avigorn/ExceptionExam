from datetime import datetime
import phonenumbers
from phonenumbers.phonenumberutil import NumberParseException
import re


class Inputs:
    full_name = input('Введите ФИО: ').title()
    name = full_name.split()
    if len(name) != 3:
        raise Exception('Ошибка при вводе ФИО')
    if re.match(r'[0-9], /./', full_name):
        raise Exception('Введено не имя')

    try:
        birth_date = input('Введите дату рождения в формате YYYY-MM-DD: ')
        datetime.strptime(birth_date, '%Y-%m-%d')
    except ValueError:
        raise ValueError('Некорректная дата')

    phone_number = input("Введите номер телефона начиная с плюса: ")
    number = phonenumbers.parse(str(phone_number), region=None, keep_raw_input=False,
                                numobj=None, _check_region=False)
    if not re.match(r'[+]', str(phone_number)):
        raise NumberParseException(1, 'Отсутствует плюс')
    elif len(str(phone_number)) > 12:
        raise NumberParseException(4, 'Слишком длинный номер')
    elif len(str(phone_number)) < 12:
        raise NumberParseException(3, 'Слишком короткий номер')
    elif re.match(r'[a-z], [A-Z], [а-я], [А-Я]', phone_number):
        raise ValueError('Вы ввели не номер')

    sex = input("Выберите пол (М/Ж): ").title()
    match sex:
        case 'М':
            sex = "Мужчина"
        case 'Ж':
            sex = 'Женщина'
    if not re.match(r'[М]|[Ж]', sex):
        raise ValueError("Некорректный выбор")
