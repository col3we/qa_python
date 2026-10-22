from address import Address
from mailing import Mailing

sender_address = Address(
    index="101000",
    city="Москва",
    street="Никольская",
    building="1",
    apartment="10"
)

recipient_address = Address(
    index="190000",
    city="Санкт-Петербург",
    street="Невский проспект",
    building="50",
    apartment="5"
)

mailing_item = Mailing(
    to_address=recipient_address,
    from_address=sender_address,
    cost=450.50,
    track="RU123456789US"
)

print(
    f"Отправление {mailing_item.track} из "
    f"{mailing_item.from_address.index}, {mailing_item.from_address.city}, "
    f"{mailing_item.from_address.street}, {mailing_item.from_address.building} - "
    f"{mailing_item.from_address.apartment} в "
    f"{mailing_item.to_address.index}, {mailing_item.to_address.city}, "
    f"{mailing_item.to_address.street}, {mailing_item.to_address.building} - "
    f"{mailing_item.to_address.apartment}. "
    f"Стоимость {mailing_item.cost} рублей."
)
