from address import Address
from Mailing import Mailing

from_address = Address("123456", "Москва", "Ленина", "10", "1")
to_address = Address("678945", "Пермь", "Пушкина", "5", "9")

mail = Mailing(
    to_address,
    from_address,
    cost=150.50,
    track="TRK123456789"
    )

print(
    "Отправление " + mail.track +
    " из " + mail.from_address.index +
    ", " + mail.from_address.city +
    ", " + mail.from_address.street +
    ", " + mail.from_address.house +
    " - " + mail.from_address.apartment +
    " в " + mail.to_address.index +
    ", " + mail.to_address.city + ", " +
    mail.to_address.street +
    ", " + mail.to_address.house +
    " - " + mail.to_address.apartment +
    ". Стоимость " + str(mail.cost) + " рублей."
)
