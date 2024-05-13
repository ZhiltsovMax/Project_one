import re
from datetime import datetime

def register():
    name = input("Введите ваше имя (от 6 до 30 символов, используйте буквы латинского алфавита, цифры и точки): ")
    while not re.match(r'^[a-zA-Z0-9.]{6,30}$', name):
        name = input("Некорректное имя. Попробуйте снова: ")

    surname = input("Введите вашу фамилию (от 6 до 30 символов, используйте буквы латинского алфавита, цифры и точки): ")
    while not re.match(r'^[a-zA-Z0-9.]{6,30}$', surname):
        surname = input("Некорректная фамилия. Попробуйте снова: ")

    while True:
        try:
            birth_date = input("Введите вашу дату рождения в формате дд-мм-гггг: ")
            birth_date_obj = datetime.strptime(birth_date, '%d-%m-%Y')
            age = datetime.now().year - birth_date_obj.year
            if age < 18 or age > 60:
                print("Ваш возраст не подходит для регистрации. Вам должно быть от 18 до 60 лет.")
            else:
                print("Ваш возраст подходит для регистрации.")
                break
        except ValueError:
            print("Некорректный формат даты. Попробуйте снова.")

    gender = input("Введите ваш пол (мужской или женский): ")
    while gender.lower() not in ['мужской', 'женский']:
        gender = input("Некорректный пол. Введите мужской или женский: ")

    city = input("Введите ваш город: ")

    email = input("Введите ваш email: ")
    while not re.match(r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$', email):
        email = input("Некорректный email. Попробуйте снова: ")

    username = input("Введите ваш логин: ")

    password = input("Введите ваш пароль: ")
    confirm_password = input("Повторите ваш пароль: ")
    while password != confirm_password:
        print("Пароли не совпадают. Попробуйте снова.")
        password = input("Введите ваш пароль: ")
        confirm_password = input("Повторите ваш пароль: ")

    print("Регистрация успешно выполнена!")

register()
