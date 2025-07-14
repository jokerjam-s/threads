# Напишите функцию для вычисления факториала, передаваемого числа.
# Для имитации длительности работы используйте задержку в размере 1/10 от передаваемого в функцию числа.
# Для конкуретного выполнения задач используйте пул потоков. Выведите в консоль результаты по мере их готовности, в виде:
#           Факториал числа <число> равен <результат>
#
# Используйте следующую последовательность: [5, 4, 7, 6, 3]
from concurrent.futures import ThreadPoolExecutor, as_completed
from time import sleep

numbers = [5, 4, 7, 6, 3]


def factorial(n):
    sleep(n / 10)
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)


def main():
    with ThreadPoolExecutor(max_workers=10) as executor:
        futures = {executor.submit(factorial, n): n for n in numbers}

        for future in as_completed(futures.keys()):
            print(f'Факториал числа {futures.get(future)} равен {future.result()}')


if __name__ == '__main__':
    main()
