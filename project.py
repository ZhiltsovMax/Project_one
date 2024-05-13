class UserRegistration:
    def __init__(self):
        self.name = ""
        self.surname = ""
        self.birth_date = ""
        self.gender = ""
        self.email = ""
        self.username = ""
        self.password = ""
        self.confirm_password = ""

    def register_user(self):
        self.name = input("Введите ваше имя: ")
        self.surname = input("Введите вашу фамилию: ")
        self.birth_date = input("Введите вашу дату рождения: ")
        self.gender = input("Введите ваш пол: ")
        self.email = input("Введите ваш E-mail: ")
        self.username = input("Введите ваш логин: ")
        self.password = input("Введите ваш пароль: ")
        self.confirm_password = input("Повторите ваш пароль: ")

        if self.password != self.confirm_password:
            print("Пароли не совпадают. Попробуйте снова.")
            self.register_user()
        else:
            print("Регистрация прошла успешно!")

user = UserRegistration()
user.register_user()