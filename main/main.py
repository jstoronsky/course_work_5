from src.db_queries import DBManager


query1 = DBManager()
# query1.get_companies_and_vacancies_count()  # список всех компаний и количество вакансий у каждой компании
query1.get_all_vacancies()  # список всех вакансий
query1.get_avg_salary()  # средняя зарплата
# query1.get_vacancies_with_higher_salary()  # список всех вакансий, у которых зарплата выше средней
# query1.get_vacancies_with_keyword('менеджер')  # список всех вакансий, в названии которых содержится ключевое слово
DBManager.connection.close()  # закрытие соединения с базой данных
