class Vacancy:
    """класс для работы с вакансиями"""
    name: str
    data_base: str
    salary: int
    city: str
    result: list

    def __init__(self, name, salary, city, data_base, result):
        """инициализатор класса vacancy"""
        self.name = name
        self.salary = salary
        self.city = city
        self.result = []
        self.data_base = data_base
        self.__reform_file(self.data_base)

    def __reform_file(self, data):
        """обработка json-ответа от hh.ru"""
        for i in data:
            if i["salary"] is None or i["salary"] == 0:
                self.result.append({
                    "name": i["name"],
                    "salary": {"from": 0,
                               "to": 0},
                    "city": i["area"]["name"],
                    "url": i["alternate_url"],
                    "descripcion": i["snippet"]["requirement"]
                })
            elif i["salary"]["from"] is None and i["salary"]["currency"] == 'RUR':
                self.result.append({
                    "name": i["name"],
                    "salary": {"from": 0,
                               "to": i["salary"]["to"]},
                    "city": i["area"]["name"],
                    "url": i["alternate_url"],
                    "description": i["snippet"]["requirement"]
                })
            elif i["salary"]["to"] is None and i["salary"]["currency"] == 'RUR':
                self.result.append({
                    "name": i["name"],
                    "salary": {"from": i["salary"]["from"],
                               "to": 0},
                    "city": i["area"]["name"],
                    "url": i["alternate_url"],
                    "description": i["snippet"]["requirement"]
                })
            elif i["salary"]["currency"] == "RUR":
                self.result.append({
                    "name": i["name"],
                    "salary": {"from": i["salary"]["from"],
                               "to": i["salary"]["to"]},
                    "city": i["area"]["name"],
                    "url": i["alternate_url"],
                    "description": i["snippet"]["requirement"]
                })

    def __le__(self, other, my_list):
        res_salary = []
        for i in my_list:
            if other <= i["salary"]["from"]:
                res_salary.append(i)
        return res_salary

    def filter_by_city(self):
        result_city = []
        for i in self.result:
            if self.city == i["city"]:
                result_city.append(i)
        return result_city
