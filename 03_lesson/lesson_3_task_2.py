from smartphone import Smartphone

catalog = []
phone1 = Smartphone("Samsung", "A51", "+79120001122")
phone2 = Smartphone("Huawie", "Nova", "+79612223344")
phone3 = Smartphone("Poco", "x3 pro", "+79221112233")
phone4 = Smartphone("iPhone", "XR", "+79045556677")
phone5 = Smartphone("Nokia", "3310", "+79187777777")

catalog.append(phone1)
catalog.append(phone2)
catalog.append(phone3)
catalog.append(phone4)
catalog.append(phone5)

for phone in catalog:
    print(f"Телефон: {phone.Marka} - {phone.Model}. \nНомер: {phone.Number}")