--1
SELECT employer_name, open_vacancies FROM employers;

--2
SELECT vacancies.vacancy_name, employers.employer_name, vacancies.salary, vacancies.link FROM
vacancies INNER JOIN employers USING(employer_id);

--3
SELECT AVG(salary) AS avg_salary FROM vacancies;

--4
SELECT * FROM vacancies WHERE salary > (SELECT AVG(salary) FROM vacancies);

--5
SELECT * FROM vacancies WHERE vacancy_name LIKE '%Менеджер%';