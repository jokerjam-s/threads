from concurrent.futures import ThreadPoolExecutor, as_completed

small_numbers = list(range(1, 51))
medium_numbers = list(range(51, 151))
large_numbers = list(range(151, 301))


# Функции для обработки чисел
def square(number):
    return number * number


def cube(number):
    return number ** 3


def factorial(number):
    return number * factorial(number - 1) if number > 1 else 1


# Функция для обработки числа с использованием заданной функции
def process_number(number, function):
    return {number: function(number)}


# Обработка списков с разными функциями и размерами пулов
results_small = list()
results_medium = list()
results_large = list()

def process_number_thread(numbers: list, function, result: list, pool_size):
    with ThreadPoolExecutor(max_workers=pool_size) as executor:
        futures = [executor.submit(process_number, number, function) for number in numbers]

        for future in as_completed(futures):
            result.append(future.result())


def main():
    process_number_thread(small_numbers, square, results_small, 50)
    process_number_thread(medium_numbers, cube, results_medium, 150)
    process_number_thread(large_numbers, factorial, results_large, 300)


    # Вывод результатов
    print("Результаты для маленьких чисел (возведение в квадрат):")
    for result in results_small:
        print(result)

    print("\nРезультаты для средних чисел (возведение в куб):")
    for result in results_medium:
        print(result)

    print("\nРезультаты для больших чисел (факториал):")
    for result in results_large:
        print(result)


if __name__ == "__main__":
    main()
