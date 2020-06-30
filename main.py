from application import salary
from db import people
import datetime

def budget():
    budget_salary = (salary.calculate_salary() * people.get_employees())
    return budget_salary

if __name__ == '__main__':
    print('Общий зарплатный бюджет всех сотрудников составляет: ', budget())
    print('Текущая дата :', datetime.datetime.today())