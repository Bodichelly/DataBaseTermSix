def translate_city_name(city: str) -> str:
    return city_dictionary[city]


city_dictionary = {
    'Киев': 'Kyiv',
    'Львов': 'Lviv',
    'Другой': 'Another',
    'Днепр': 'Dnipro',
    'Харьков': 'Kharkiv',
    'Одесса': 'Odessa',
    'Запорожье': 'Zaporizhya',
    'Удаленно': 'Another',
    'Черновцы': 'Chernivtsi',
    'Полтава': 'Poltava',
    'Хмельницкий': 'Khmelnitsky',
    'Ровно': 'Rivne',
    'Николаев': 'Mykolaiv',
    'Винница': 'Vinnitsa',
    'Сумы': 'Sumy',
    'Херсон': 'Kherson',
    'Житомир': 'Zhytomyr',
    'Черкассы': 'Cherkasy',
    'Ивано-Франковск': 'Ivano-Frankivsk',
    'Кропивницкий': 'Kropyvnytskyi',
    'Тернополь': 'Ternopil',
    'Ужгород': 'Uzhgorod',
    'Луцк': 'Lutsk',
    'Чернигов': 'Chernihiv',
    'Мариуполь': 'Mariupol',
    'Кривой Рог': 'Kryvyi Rih',
    'Севастополь': 'Sevastopol',
    'Луганск': 'Lugansk',
    'Донецк': 'Donetsk',
    'Симферополь': 'Simferopol',
    'Кировоград': 'Kirovograd',
    'Тирасполь': 'Another'
}
