from src.vacancy_api import HH
from src.vacancy import Vacancy
from src.vacancy_json import HHVacancy
from src.utils import top_vacancy, filter_vacancy


def user_interaction():
    """Функция для взаимодействия с клиентом"""
    search_query = input("Введите поисковый запрос: ")
    hh = HH()
    city_search = input("Введите город для поиска вакансии: ")
    hh.load_vacancies(search_query)
    filter_words = input("Введите ключевые слова для фильтрации вакансий: ").split()
    salary = int(input("Введите желаемую зарплату: "))
    top_n = input("Введите количество вакансий для вывода в топ N: ")
    vacancy = Vacancy(search_query, city_search, salary,hh.vacancies)
    res_city = vacancy.filter_by_city()
    res_salary = vacancy.__le__(salary, res_city)
    result_fil_words = filter_vacancy(res_salary, filter_words)
    sd = HHVacancy()
    sd.safe_vacancy(result_fil_words)
    result_of_top = top_vacancy(top_n, result_fil_words)
    del_vacancy = input("Требуется что-нибудь удалить из файла? 'Да,Нет': ")
    if del_vacancy == 'Да':
        words_del = input('Введите ключевые слова для удаления вакансий(Название вакансии,город и т.п): ')
        sd.delete_vacancy(words_del)
    fit_back = input("Требуется определенная выборка для вывода, или все данные из файла? 'Определенные,Все': ")
    if fit_back == 'Определенные':
        words_sample = input("Введите ключевое слово для выборки данных(Город, название вакансии и т.п): ")
        sd.vacancy_from_file(words_sample)
    elif fit_back == "Все":
        sd.full_data_from_file()
    return result_of_top


print(user_interaction())