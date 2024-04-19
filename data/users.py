class User:

    def __init__(self, name, family, address, metro_station, phone, date, lease_period, color, comment):
        self.name = name
        self.family = family
        self.address = address
        self.metro_station = metro_station
        self.phone = phone
        self.date = date
        self.lease_period = lease_period
        self.color = color
        self.comment = comment



user1 = User(
    'Вассиссуалий',
    'Пупкин',
    'на деревню в дедушке',
    'Сокольники',
    '89001112233',
    '30.04.2024',
    'трое суток',
    'серая безысходность',
    'позвоните за полчаса'
)

user2 = User(
    'Иван',
    'Петров',
    '3-я Песчаная улица, 2А',
    'Зорге',
    '89886537809',
    '09.05.2024',
    'сутки',
    'чёрный жемчуг',
    'не звонить, оставьте под дверью'
)