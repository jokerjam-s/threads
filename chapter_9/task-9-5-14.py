import os
from multiprocessing import Pool


def read_and_sum(filename):
    with open(filename) as f:
        numbers = int(f.readline())
    return numbers


def sum_numbers_in_files(directory):
    files = os.listdir(directory)

    with Pool(4) as pool:
        results = pool.map(read_and_sum, [directory + '/' + file for file in files])
        total = sum(results)
        print(f"Общая сумма чисел в файлах: {total}")


def main():
    sum_numbers_in_files('./files')


if __name__ == '__main__':
    main()
