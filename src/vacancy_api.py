import json

from abc import ABC, abstractmethod
import requests


class Parser(ABC):
    """Родительский класс get-запросов"""

    @abstractmethod
    def load_vacancies(self, keyword):
        """Метод отправки get-запроса на сайт Head Hunter"""
        pass


class HH(Parser):
    """Класс для работы с API HeadHunter"""

    def __init__(self):
        """Магический метод инициализаций объектов для отправки get-запроса"""
        self._url = 'https://api.hh.ru/vacancies'
        self._headers = {'User-Agent': 'HH-User-Agent'}
        self.params = {'text': '', 'page': 0, 'per_page': 100}
        self.vacancies = []

    def load_vacancies(self, keyword):
        """Метод отправки get-запроса на сайт Head Hunter"""
        self.params['text'] = keyword
        while self.params.get('page') != 20:
            response = requests.get(self._url, headers=self._headers, params=self.params)
            vacancies = response.json()['items']
            self.vacancies.extend(vacancies)
            self.params['page'] += 1