from cgitb import reset

import pytest
import json
from src.vacancy import Vacancy

with open('data_tests.json', 'r', encoding="utf-8") as file:
    data = json.load(file)

@pytest.fixture
def valid():
    """Фикстура для метода валидации класса HH()"""
    test_vac = Vacancy('Разработчик','Москва',20000,data, result)
    return test_vac

@pytest.fixture
def city():
    """Фикстура для метода фильтрации по городу класса HH()"""
    test_vac = Vacancy('Разработчик', 'Москва', 20000, data, result)
    return test_vac.filter_by_city()

@pytest.fixture
def difference():
    """Фикстура для метода фильтрации по заработной плате класса HH()"""
    test_vac = Vacancy('Разработчик', 'Москва', 120000, data)
    city_1 = test_vac.filter_by_city()
    dif = test_vac.__le__(120000, city_1)
    return dif