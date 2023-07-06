import requests
import json


def get_employer_data():
    """
    функция, реализующая получение через API отформатированного словаря с информацией о
    10 выбранных работодателях
    """
    from_hh = requests.get('https://api.hh.ru/employers?area=40&page=30&per_page=100&only_with_vacancies=true')
    python_type = json.loads(from_hh.text)
    final_data = {'id': [emp['id'] for emp in python_type['items'][-10:]],
                  'employer_name': [name['name'] for name in python_type['items'][-10:]],
                  'open_vacancies': [op['open_vacancies'] for op in python_type['items'][-10:]]}
    return final_data


employer_data = get_employer_data()


def get_vacancies_data():
    """
    функция, реализующая получение через API отформатированного словаря с информацией о
    вакансиях, которые разместили выбранные нами работодатели
    """
    vacancies_id = []
    vacancies_names = []
    employer_id = []
    area = []
    salary = []
    links = []
    for id_ in employer_data['id']:
        from_hh_ = requests.get('https://api.hh.ru/vacancies?employer_id={}'.format(id_))
        python_type_ = json.loads(from_hh_.text)
        vacancies_id.extend([vac['id'] for vac in python_type_['items']])
        vacancies_names.extend([name['name'] for name in python_type_['items']])
        employer_id.extend([emp['employer']['id'] for emp in python_type_['items']])
        area.extend([place['area']['name'] for place in python_type_['items']])
        for salary_ in python_type_['items']:
            if salary_['salary'] is not None:
                if salary_['salary']['to'] is None:
                    salary.append(salary_['salary']['from'])
                else:
                    salary.append(salary_['salary']['to'])
            else:
                salary.append(0)
        links.extend([f"https://hh.ru/vacancy/{vac['id']}" for vac in python_type_['items']])
    final_data = dict(zip(('vacancy_id', 'vacancy_name', 'employer_id', 'salary', 'city', 'link'),
                          (vacancies_id, vacancies_names, employer_id, salary, area, links)))
    return final_data
