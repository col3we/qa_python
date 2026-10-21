from address import Address


class Mailing:
    def __init__(self, to_address: Address, from_address: Address, cost: float, track: str):
        """
        :param to_address: адрес получателя (объект Address)
        :param from_address: адрес отправителя (объект Address)
        :param cost: стоимость отправления
        :param track: трек-номер
        """
        self.to_address = to_address
        self.from_address = from_address
        self.cost = cost
        self.track = track
