import csv
import platform
import os
from src.get_data_from_hh import employer_data, get_vacancies_data


vacancies_data = get_vacancies_data()


def write_employer_data_to_csv(file_name):
    """
    запись информации о работодателях в csv файл,
    дополнительно составлены два варианта пути(для UNIX-подобных и Windows,
    куда будет сохранён файл для лучшей переносимости кода
    """
    if platform.system() != 'Windows':
        path = os.path.join('/tmp', file_name)
    else:
        path = os.path.join('C:', 'Users', 'Public', file_name)
    with open(path, 'w', newline='') as csv_file:
        fieldnames = ['id', 'employer_name', 'open_vacancies']
        to_csv = csv.DictWriter(csv_file, fieldnames=fieldnames)
        to_csv.writeheader()
        for index in range(len(employer_data['id'])):
            to_csv.writerow({'id': employer_data['id'][index],
                             'employer_name': employer_data['employer_name'][index],
                             'open_vacancies': employer_data['open_vacancies'][index]})


def write_vacancy_data_to_csv(file_name):
    """
    запись информации о вакансиях в csv файл
    """
    if platform.system() != 'Windows':
        path = os.path.join('/tmp', file_name)
    else:
        path = os.path.join('C:', 'Users', 'Public', file_name)
    with open(path, 'w', newline='') as csv_file:
        fieldnames = ['vacancy_id', 'vacancy_name', 'employer_id', 'salary', 'city', 'link']
        to_csv = csv.DictWriter(csv_file, fieldnames=fieldnames)
        to_csv.writeheader()
        for index in range(len(vacancies_data['vacancy_id'])):
            to_csv.writerow({'vacancy_id': vacancies_data['vacancy_id'][index],
                             'vacancy_name': vacancies_data['vacancy_name'][index],
                             'employer_id': vacancies_data['employer_id'][index],
                             'salary': vacancies_data['salary'][index],
                             'city': vacancies_data['city'][index],
                             'link': vacancies_data['link'][index]})
