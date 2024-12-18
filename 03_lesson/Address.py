class Address:

    def __init__(self, Index, City, Street, House, Apartment):
        self.index = Index
        self.town = City
        self.ulitsa = Street
        self.dom = House
        self.kv = Apartment

    def __str__(self):
        return (f"{self.index}, {self.town}, {self.ulitsa}"
                f"{self.dom}, {self.kv}")