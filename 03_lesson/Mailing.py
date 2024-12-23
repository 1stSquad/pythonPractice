class Mailing:

    def __init__(self,  track, to_address, from_address, cost):
        self.cuda = to_address
        self.otkuda = from_address
        self.cena = cost
        self.track_number = track

    def __str__(self):
        return (f"Отправление {self.track_number} из: {self.otkuda}"
                f"В {self.cuda}. Цена: {self.cena} рублей")