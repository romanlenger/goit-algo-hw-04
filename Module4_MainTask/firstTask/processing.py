from preparingData import get_raw_data, get_salary


def total_salary(filepath: str) -> tuple:
    salary_list = get_salary(get_raw_data(filepath))

    total = sum(salary_list)
    average = sum(salary_list) // len(salary_list)

    return total, average 
