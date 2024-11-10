from abc import ABC, abstractmethod

import json
import os.path


class JSONVacancy(ABC):
    """Абстрактный метод для создания и удаления JSON-файлов"""

    @abstractmethod
    def safe_vacancy(self, stock_list):
        """Метод для сохранения данных о вакансиях в файл"""
        pass

    @abstractmethod
    def delete_vacancy(self,words_del):
        """Метод для удаления не нужного файла"""
        pass


class HHVacancy(JSONVacancy):
    """Класс для создания и удаления файлов с данными по вакансиям из сайта HH.ru"""

    def __init__(self,file_name_save = 'data/suitable_vacancies.json'):
        """Инициализатор класса"""
        self.__file_name_save = file_name_save
    def get_file_name(self):
        return self.__file_name_save

    def safe_vacancy(self, stock_list):
        """Метод для сохранения данных о вакансиях в файл"""
        if stock_list is None:
            print("Вакансий с такими критериями не найдено")
        elif stock_list is not None:
            if os.path.exists(self.get_file_name()):
                with open(self.get_file_name(), 'r', encoding="utf-8") as file:
                    data = json.load(file)
                for i in stock_list:
                    if i not in data:
                        data.append(i)
                with open(self.get_file_name(), 'w', encoding="utf-8") as file:
                    json.dump(data, file, indent=4,
                              ensure_ascii=False)
            else:
                with open(self.get_file_name(), 'w', encoding="utf-8") as file:
                    json.dump(stock_list, file, indent=4, ensure_ascii=False)

    def delete_vacancy(self, words_del):
        """Метод для удаления не нужных данных из файла"""
        data_1 = []
        if os.path.exists('../data/suitable_vacancies.json'):
            with open(self.get_file_name(), 'r', encoding="utf-8") as file:
                data = json.load(file)
            for i in data:
                if words_del != i['city'] and words_del not in i['name'] and words_del not in i['description']:
                    data_1.append(i)
            with open(self.get_file_name(), 'w', encoding="utf-8") as file:
                json.dump(data_1, file, indent=4,
                          ensure_ascii=False)
            return data_1
        else:
            return 'Файла с таким название не существует'

    def vacancy_from_file(self, words_sample):
        """Метод для выборки нужных данных из файла"""
        result_data = []
        if os.path.exists(self.get_file_name()):
            with open(self.get_file_name(), 'r', encoding="utf-8") as file:
                data = json.load(file)
            for i in data:
                if words_sample in i["description"] or words_sample == i['name'] or words_sample == i['city']:
                    result_data.append(i)

            return result_data
        else:
            return 'Файла с таким название не существует'
    def full_data_from_file(self):
        if os.path.exists(self.get_file_name()):
            with open(self.get_file_name(), 'r', encoding="utf-8") as file:
                data = json.load(file)
            return data
        else:
            "Файл пуст"