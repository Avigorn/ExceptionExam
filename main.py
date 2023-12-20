from inputs import Inputs


class Main:

    with open('Book.txt', 'a+', encoding='utf-8') as book:
        book.write(f'Фамилия: {Inputs.name[0]}\n'
                   f'Имя: {Inputs.name[1]}\n'
                   f'Отчество: {Inputs.name[2]}\n'
                   f'Дата рождения: {Inputs.birth_date}\n'
                   f'Номер телефона: {Inputs.phone_number}\n'
                   f'Пол: {Inputs.sex}\n')
