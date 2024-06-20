from processing import total_salary


def main():
    path = r'D:\GOIT New\Module4_MainTask\firstTask\staff.txt'

    total, average = total_salary(path)
    print(f"Загальна сума заробітної плати: {total}, Середня заробітна плата: {average}")


if __name__ == '__main__':
    main()