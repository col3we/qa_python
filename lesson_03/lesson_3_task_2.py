from smartphone import Smartphone

catalog = [
    Smartphone("Apple", "iPhone 11 67% battery color red refub", "+79001111337"),
    Smartphone("Samsung", "Galaxy S23 Fe", "+79004445267"),
    Smartphone("Poco", "X3 PRO", "+79007148899"),
    Smartphone("Google", "Pixel 7 Pro", "+79002223369"),
    Smartphone("Sony", "Xperia 1 V", "+79005556642")
]

for phone in catalog:
    print(f"{phone.brand} - {phone.model}. {phone.phone_number}")
