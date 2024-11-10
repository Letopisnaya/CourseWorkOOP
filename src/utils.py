def top_vacancy(number, my_list):
    """Функция вывода Топ-n вакансий для пользователя"""
    if number == "":
        return my_list
    else:
        return my_list[0:int(number)]


def filter_vacancy(my_list, words_list):
    """Функция фильтрации вакансий по ключевым словам в описании или названия вакансии"""
    fin_list = []
    for index in my_list:
        for i in words_list:
            if index["description"] is None:
                continue
            elif i in index["description"] or i in index["name"]:
                fin_list.append(index)
    return fin_list