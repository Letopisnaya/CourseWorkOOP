from idlelib.iomenu import encoding
from plistlib import dumps

from src.vacancy_json import HHVacancy
import json
vacan = [{
        "name": "Middle Python Developer",
        "city": "Москва",
        "salary": {
            "from": 200000,
            "to": 0
        },
        "url": "https://hh.ru/vacancy/108969522",
        "description": "FastAPI, SQLAlchemy, Pydantic (v1/v2). Scrapy. Docker, Airflow, Celery, Redis. Postgres. Опыт работы с Python от 2х..."
    },
    {
        "name": "Python разработчик",
        "city": "Санкт-Петербург",
        "salary": {
            "from": 250000,
            "to": 300000
        },
        "url": "https://hh.ru/vacancy/108168771",
        "description": "Python 3. Опыт работы с фреймворком FastAPI и с асинхронным вызовами (Asyncpg, Asyncio ...). Опыт работы с микросервисной архитектурой. Docker. PostgreSQL. "
    }]



def test_save_vacancy():
    """Тестирование метода сохранения данных в файл"""
    test_1 = HHVacancy()
    res = test_1.safe_vacancy(vacan)
    ext = None
    with open('data/suitable_vacancies.json', 'r', encoding="utf-8") as file:
        data = json.load(file)
    assert res == ext

def test_delete_vacancy():
    """Тестирование метода удаления из файла данных"""
    test_2 = HHVacancy()
    test_2.safe_vacancy(vacan)
    result = test_2.delete_vacancy('Санкт-Петербург')
    with open('data/suitable_vacancies.json', 'r', encoding="utf-8") as file:
        data = json.load(file)
    assert result == data


def test_vacancy_from_file():
    """Тестирование метод получения нужной вакансии"""
    test_3 = HHVacancy()
    test_3.safe_vacancy(vacan)
    result = test_3.vacancy_from_file('Москва')
    assert  result == [vacan[0]]

def test_full_data_from_file():
    """"""
    test_3 = HHVacancy()
    test_3.safe_vacancy(vacan)
    assert test_3.full_data_from_file() == vacan