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

    gender = input("Выберете ваш пол:\n 1)Мужской\n 2)Женский\n")
    if (gender=="1"):
        print("Ваш пол: мужской")
    if (gender=="2"):
        print("Ваш пол: женский")

    available_cities = ["Москва", "Санкт-Петербург", "Кострома"]

    def display_cities():
        print("Доступные города:")
        for index, city in enumerate(available_cities):
            print(f"{index + 1}. {city}")
        print("0. Другое")

    def add_city():
        new_city = input("Введите новый город: ")
        available_cities.append(new_city)
        print(f"Город {new_city} добавлен в список доступных городов")

    while True:
        display_cities()
        choice = input("Выберите номер города из списка: ")
        
        if choice == "0":
            add_city()
        elif choice.isdigit() and 0 < int(choice) <= len(available_cities):
            selected_city = available_cities[int(choice) - 1]
            print("Вы выбрали город", selected_city)
            break
        else:
            print("Некорректный выбор. Попробуйте снова.")


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
