from concurrent.futures import ThreadPoolExecutor

# Полная версия этого словаря вшита в задачу
students = {
    1: {'name': 'Alice', 'age': 20, 'grades': [4, 5, 5, 4, 2, 3, 5, 2]},
    2: {'name': 'Bob', 'age': 21, 'grades': [3, 4, 3, 4, 4, 5, 3, 4, 3, 2, 4]},
    3: {'name': 'Charlie', 'age': 19, 'grades': [5, 5, 5, 5, 5, 5, 4, 5, 4, 5, 4]},
    4: {'name': 'Hannah Thompson', 'age': 20, 'grades': [2, 4, 3, 5, 3, 3, 2, 4, 4, 3, 2, 2, 2, 2, 5, 3, 4, 5]}
}


# Функция для подсчета среднего балла для одного студента
def calculate_average(student_data):
    return (student_data.get('name'), round(sum(student_data.get('grades')) / len(student_data.get('grades')), 2))

def main():
    # Использование ThreadPoolExecutor для создания потоков и функции map()
    with ThreadPoolExecutor(max_workers=4) as executor:
        student_averages = dict(executor.map(calculate_average, students.values()))

    print(student_averages)

if __name__ == '__main__':
    main()