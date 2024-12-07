# Первое решение через функцию

def is_year_leap(year):
    if (year % 4 == 0):
        print(f"Год: {year} - True ")
    else:
        print(f"Год: {year} - False")

is_year_leap(2024)


# Второе решение через переменную

num = int(input("Введите год для проверки: "))

if num % 4 == 0:
    print(f"Год: {num} - True")
else:
    print(f"Год: {num} - False")