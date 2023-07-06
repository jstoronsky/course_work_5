import platform
import os
import psycopg2


def create_tables():
    """
    функция с командами для создания таблиц(работодатели и вакансии) в PostgreSQL
    """
    connection = psycopg2.connect(host='localhost', database='headhunter', user='postgres', password='dem6600')
    to_execute = (
        '''
        CREATE TABLE employers (
            employer_id int PRIMARY KEY,
            employer_name varchar(100) NOT NULL,
            open_vacancies int
           );
        ''',
        '''
        CREATE TABLE vacancies (
            vacancy_id int PRIMARY KEY,
            vacancy_name varchar(150) NOT NULL,
            employer_id int REFERENCES employers(employer_id) NOT NULL,
            salary int,
            city varchar(100),
            link varchar(200)
            );
        ''')
    try:
        with connection.cursor() as cursor1:
            for command in to_execute:
                cursor1.execute(command)
        connection.commit()
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        connection.close()


def fill_tables():
    """
    заполнение созданных таблиц информацией с csv файлов
    """
    connection = psycopg2.connect(host='localhost', database='headhunter', user='postgres', password='dem6600')
    if platform.system() != 'Windows':
        path = os.path.join('/tmp', 'employers.csv')
        path2 = os.path.join('/tmp', 'vacancies.csv')
    else:
        path = os.path.join('C:', 'Users', 'Public', 'employers.csv')
        path2 = os.path.join('C:', 'Users', 'Public', 'vacancies.csv')
    to_execute = (
        f'''
        COPY employers(employer_id, employer_name, open_vacancies)
        FROM '{path}'
        DELIMITER ','
        CSV HEADER;
        ''',
        f'''
        COPY vacancies(vacancy_id, vacancy_name, employer_id, salary, city, link)
        FROM '{path2}'
        DELIMITER ','
        CSV HEADER;
        ''')
    try:
        with connection.cursor() as cursor2:
            for command in to_execute:
                cursor2.execute(command)
        connection.commit()
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        connection.close()
