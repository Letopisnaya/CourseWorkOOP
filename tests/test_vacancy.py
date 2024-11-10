from src.vacancy import Vacancy
import json

with open('data_tests.json', 'r', encoding="utf-8") as file:
    data = json.load(file)



def test_valid(valid):
    """Тестирование метода валидации в классе HH()"""
    test_vac = Vacancy('Разработчик', 'Москва', 20000, data)
    assert test_vac == valid

def test_filter_by_city(city):
    """Тестирование метода фильтрации по городу в классе HH()"""
    test_vac = Vacancy('Разработчик', 'Москва', 20000, data)
    assert test_vac.filter_by_city() == city

def test_difference(difference):
    """Тестирование метода фильтрации по заработной плате в классе HH()"""
    test_vac = Vacancy('Разработчик', 'Москва', 120000, data)
    city_1 = test_vac.filter_by_city()
    dif = test_vac.__le__(12000,city_1)
    return dif == difference