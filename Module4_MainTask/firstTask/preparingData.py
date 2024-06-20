try:
    from termcolor import colored
except ImportError:
    colored = None


def get_raw_data(path: str) -> list[str]:
    try:
        with open(path, mode='r', encoding='utf-8') as f:
            return f.readlines()
        
    except FileNotFoundError:

        if colored:
            print(colored('Файл не знайдено!', color='yellow'))
        else:
            print('Файл не знайдено!')


def get_salary(stafflist: list[str]) -> list[int]:
    try:
        return [int(s.split(',')[1]) for s in stafflist]
    except:
        pass


