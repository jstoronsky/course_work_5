from src.to_csv_functions import write_employer_data_to_csv, write_vacancy_data_to_csv
from src.db_operations import create_tables, fill_tables

write_employer_data_to_csv('employers.csv')  # запись в csv файл информации о работодателях
write_vacancy_data_to_csv('vacancies.csv')   # запись в csv файл информации о вакансиях

create_tables()  # создание таблиц
fill_tables()  # заполнение таблиц
