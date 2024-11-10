from src.utils import top_vacancy, filter_vacancy

my_list = [
    {
        "name": "Программист Python(Middle)",
        "city": "Москва",
        "salary": {
            "from": 100000,
            "to": 200000
        },
        "url": "https://hh.ru/vacancy/108638168",
        "description": "Отличное понимание Telegram API. Опыт разработки на Python от 2 лет. Уверенное владение Python. Опыт работы с Linux (SSH). "
    },
    {
        "name": "Backend-разработчик / Разработчик Python",
        "city": "Санкт-Петербург",
        "salary": {
            "from": 230000,
            "to": 0
        },
        "url": "https://hh.ru/vacancy/109292967",
        "description": "Высшее образование в области математики или информатики (магистр или специалист). Уверенное владение Python (либо альтернативными языками и технологиями). "
    }
]

def test_top_vacancy():
    """Тестирование функции выбора топ-n вакансий для пользователя"""
    assert top_vacancy(number="", my_list=[1, 2, 3]) == [1, 2, 3]
    assert top_vacancy(number=2, my_list=[1, 2, 3]) == [1, 2]


def test_filter_vacancy():
    """Тестирование функции фильтрации вакансий по описанию и названию"""
    assert filter_vacancy(my_list=my_list, words_list=['Разработчик']) == [{
        "name": "Backend-разработчик / Разработчик Python",
        "city": "Санкт-Петербург",
        "salary": {
            "from": 230000,
            "to": 0
        },
        "url": "https://hh.ru/vacancy/109292967",
        "description": "Высшее образование в области математики или информатики (магистр или специалист). Уверенное владение Python (либо альтернативными языками и технологиями). "
    }]