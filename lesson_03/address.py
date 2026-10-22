class Address:
    def __init__(self, index: str, city: str, street: str, building: str, apartment: str):
        """
        :param index: почтовый индекс
        :param city: город
        :param street: улица
        :param building: дом
        :param apartment: квартира
        """
        self.index = index
        self.city = city
        self.street = street
        self.building = building
        self.apartment = apartment
