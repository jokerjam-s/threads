# Напишите функцию, которая будет принимать 2 аргумента: время работы (имитация) и список чисел.
# Возвращаемое значение будет зависеть от времени работы - если время работы четное число,
# то функция возвращает произведение чисел, если же нечетное - сумму чисел;
# Используйте пул потоков для одновременного выполнения целевых функций для вычислений по каждому списку из numbers;
# Выведите результаты вычислений тех функций, работа которых не превышает 2.5 секунд.
import math
from concurrent.futures import ThreadPoolExecutor, wait
from time import sleep

work_times = [4, 5, 3, 5, 4, 2, 5, 1, 3, 5, 3, 5, 1, 5, 5, 2, 1, 5, 1, 2]

numbers = [[2, 5], [6, 2], [9, 4], [2, 2], [2, 8], [3, 5], [4, 1], [6, 2],
           [7, 4], [9, 7], [5, 7], [3, 8], [4, 0], [8, 2], [6, 9], [9, 7],
           [3, 6], [6, 7], [2, 5], [7, 3]]


def calc(time_work: int, numbers: list):
    sleep(time_work)
    if time_work % 2 == 0:
        return math.prod(numbers)
    else:
        return sum(numbers)

def main():
    with ThreadPoolExecutor(max_workers=20) as executor:
        threads = [executor.submit(calc, t, n) for t, n in zip(work_times, numbers)]
        done, not_done = wait(threads, timeout=2.5)

        for future in done:
            print(future.result())

if __name__ == '__main__':
    main()