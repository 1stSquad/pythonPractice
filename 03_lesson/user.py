class User:

    def __init__(self, first_name, last_name):
        self.user_first = first_name
        self.user_last = last_name

    def show_FName(self):
        print(f"Имя: ", self.user_first)

    def show_LName(self):
        print(f"Фамилия: ", self.user_last)

    def show_All(self):
        print(f"Пользователь: ", self.user_first, self.user_last)