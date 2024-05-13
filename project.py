import re

def register():
    name = input("Введите ваше имя (от 6 до 30 символов, используйте буквы латинского алфавита, цифры и точки): ")
    while not re.match(r'^[a-zA-Z0-9.]{6,30}$', name):
        name = input("Некорректное имя. Попробуйте снова: ")

    surname = input("Введите вашу фамилию (от 6 до 30 символов, используйте буквы латинского алфавита, цифры и точки): ")
    while not re.match(r'^[a-zA-Z0-9.]{6,30}$', surname):
        surname = input("Некорректная фамилия. Попробуйте снова: ")

    birth_date = input("Введите вашу дату рождения в формате дд-мм-гггг: ")
    # Дополнительные проверки для возраста могут быть добавлены

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
