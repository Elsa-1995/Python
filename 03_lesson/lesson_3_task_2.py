from smartphone import Smartphone

catalog = [
    Smartphone('iphone', 'se', '+79991112233'),
    Smartphone('samsung', 'k1', '+71112223344'),
    Smartphone('yl', 't3', '+72223334455'),
    Smartphone('moto', 'x5', '+73332223344'),
    Smartphone('readme', 'x5', '+79261234567')
]

for smartphone in catalog:
    print(f'{Smartphone.brand} - {Smartphone.model}. {Smartphone.number}')
