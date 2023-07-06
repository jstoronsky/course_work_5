import psycopg2


class DBManager:
    """
    класс с методами, позволяющими получить через запросы конкретную информацию с таблиц PostgreSQL
    """
    connection = psycopg2.connect(host='localhost', database='headhunter', user='postgres', password='dem6600')

    def get_companies_and_vacancies_count(self):
        """
        получает список всех компаний и количество вакансий у каждой компании
        """
        with self.connection.cursor() as cursor:
            cursor.execute('''SELECT employer_name, open_vacancies FROM employers;''')
            query = cursor.fetchall()
        self.connection.commit()
        for data in query:
            print(f'Работодатель: {data[0]}, открытых вакансий: {data[1]}')

    def get_all_vacancies(self):
        """
        получает список всех вакансий с указанием названия компании, названия вакансии и зарплаты и ссылки на вакансию
        """
        with self.connection.cursor() as cursor:
            cursor.execute('''SELECT 
            vacancies.vacancy_name, employers.employer_name, vacancies.salary, vacancies.link 
            FROM vacancies INNER JOIN employers USING(employer_id);''')
            query = cursor.fetchall()
        self.connection.commit()
        for data in query:
            print(f'Вакансия: {data[0]}, Работодатель: {data[1]}, Зарплата: {data[2]}, Ссылка: {data[3]}')

    def get_avg_salary(self):
        """
        получает среднюю зарплату по вакансиям
        """
        with self.connection.cursor() as cursor:
            cursor.execute('''SELECT ROUND(AVG(salary)) AS avg_salary FROM vacancies;''')
            query = cursor.fetchall()
        self.connection.commit()
        for data in query:
            print(f'Средняя зарплата: {data[0]}')

    def get_vacancies_with_higher_salary(self):
        """
        получает список всех вакансий, у которых зарплата выше средней по всем вакансиям
        """
        with self.connection.cursor() as cursor:
            cursor.execute('''
                SELECT vacancy_name, salary, city, link
                FROM vacancies WHERE salary > (SELECT AVG(salary) FROM vacancies);''')
            query = cursor.fetchall()
        self.connection.commit()
        print('Вакансии, у которых ЗП выше чем средняя:\n')
        for data in query:
            print(f'{data[0]}, зарплата: {data[1]}, город: {data[2]}, ссылка: {data[3]}')

    def get_vacancies_with_keyword(self, keyword):
        """
        получает список всех вакансий, в названии которых содержится переданное в метод слово
        """
        with self.connection.cursor() as cursor:
            cursor.execute(f''' 
            SELECT vacancy_name, salary, city, link 
            FROM vacancies WHERE vacancy_name LIKE '%{keyword}%';;''')
            query = cursor.fetchall()
        self.connection.commit()
        print('Вакансии по указанному ключевому слову:\n')
        if len(query) != 0:
            for data in query:
                print(f'{data[0]}, зарплата: {data[1]}, город: {data[2]}, ссылка: {data[3]}')
        else:
            raise Exception('Нет информации по данному ключевому слову')
