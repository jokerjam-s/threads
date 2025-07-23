import os
import threading
from multiprocessing import Pool


def have_zero(numbers: list[int]) -> bool:
    for number in numbers:
        if number == 0:
            return True
    return False


def file_working(filename: str):
    with open(filename) as f:
        numbers = [int(n) for n in f.readlines()]

    res = 1
    if have_zero(numbers):
        res = sum(numbers) * (-1)
    else:
        for number in numbers:
            res = res * number
    return res


def calculate(directory: str):
    files = os.listdir(directory)
    files = [directory + os.sep + file for file in files]

    with Pool(4) as pool:
        results = pool.map_async(file_working, files)

        pool.close()
        pool.join()
    summ = sum(results.get())
    return summ


def main():
    print(calculate('.\\files2'))


if __name__ == '__main__':
    main()
