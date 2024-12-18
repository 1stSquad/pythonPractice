from Address import Address
from Mailing import Mailing

to_address = Address(125032, "Москва", "Тверская", 13, "none")

from_address = Address(350049, "Краснодар", "Карла Маркса", 39, "none")

posilka = Mailing(17934570, to_address, from_address, 359)

print(posilka)