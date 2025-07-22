from multiprocessing.pool import Pool
import time

# Полный словарь вшит в задачу

data = {'Михей Валентинович Никонов': {'Математика': 3, 'Физика': 2, 'Химия': 2, 'История': 3, 'Биология': 3,
                                       'География': 5, 'Информатика': 5, 'Литература': 5, 'Иностранный язык': 2,
                                       'Физкультура': 2},
        'Захарова Евгения Андреевна': {'Математика': 3, 'Физика': 3, 'Химия': 4, 'История': 4, 'Биология': 3,
                                       'География': 3, 'Информатика': 5, 'Литература': 3, 'Иностранный язык': 5,
                                       'Физкультура': 4},
        'Петухова Ангелина Антоновна': {'Математика': 2, 'Физика': 1, 'Химия': 1, 'История': 1, 'Биология': 2,
                                        'География': 2, 'Информатика': 4, 'Литература': 3, 'Иностранный язык': 1,
                                        'Физкультура': 2},
        'Селиверстова Любовь Семеновна': {'Математика': 5, 'Физика': 3, 'Химия': 2, 'История': 3, 'Биология': 5,
                                          'География': 4, 'Информатика': 5, 'Литература': 5, 'Иностранный язык': 3,
                                          'Физкультура': 4}}

_MIN_GRADE = 2


# Функция для обработки информации о студенте
def process_student_info(student_name: str, grades: dict[str, int]):
    avg_grade = sum(grades.values()) / len(grades)
    time.sleep(avg_grade)
    if avg_grade < _MIN_GRADE:
        raise ValueError(f"Средний балл {student_name} ниже минимального порога: {avg_grade}")

    return f"{student_name}: средний балл {avg_grade}"


# Функция обратного вызова для ошибок
def on_error(exception):
    print(exception)


# Функция обратного вызова для успешной обработки
def on_success(result):
    print(result)


def main():
    pool = Pool(4)
    [pool.apply_async
     (process_student_info, (student, data[student],), callback=on_success, error_callback=on_error)
     for student in data.keys()
     ]

    pool.close()
    pool.join()


if __name__ == "__main__":
    main()
