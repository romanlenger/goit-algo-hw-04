def get_cats_info(path: str) -> list[dict]:
    cats_info = []

    try:
        with open(path, 'r', encoding='utf-8') as file:
            for line in file:
                cat_data = line.strip().split(',')
                cat_info = {
                    "id": cat_data[0],
                    "name": cat_data[1],
                    "age": cat_data[2]
                }
                cats_info.append(cat_info)

    except FileNotFoundError:
        print("Файл не знайдено.")

    except Exception as e:
        print(f"Помилка: {e}")

    return cats_info


cats_info = get_cats_info(r'D:\GOIT New\Module4_MainTask\secondTask\cats.txt')
print(cats_info)