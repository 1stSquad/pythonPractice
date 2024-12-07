def month_to_season():
    x = int(input("Введите номер месяца: "))
    if x in [12, 1, 2]:
        print("Зима")
    elif x in [3, 4, 5]:
        print("Весна")
    elif x in [6, 7, 8]:
        print("Лето")
    elif x in [9, 10, 11]:
        print("Осень")
    else:
        print("Нет такого месяца!")

month_to_season()