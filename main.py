from application.salary import calculate_salary
from application.db.people import get_employees

def main():
    all = (calculate_salary() * get_employees())
    return print(all)



if __name__ == '__main__':
    main()