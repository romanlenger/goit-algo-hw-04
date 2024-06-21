from preparingData import get_raw_data, get_salary


def total_salary(filepath: str) -> tuple:
    salary_list = get_salary(get_raw_data(filepath))

    total = sum(salary_list)
    average = 0 if len(salary_list) == 0 else total // len(salary_list) #ZeroDivisionError

    return total, average 
