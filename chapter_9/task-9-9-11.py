import os
from multiprocessing import Pool
from multiprocessing.pool import ThreadPool


def get_list_files(directory: str) -> list:
    files = os.listdir(directory)
    return [directory + os.sep + file for file in files]


def read_number(file: str, start_path: str) -> int:
    print(file)
    with open(file, 'r', encoding='utf-8') as f:
        path = start_path + os.sep + f.readline()
        print(path)

    with open(path, 'r', encoding='utf-8') as fl:
        num = int(fl.readline())

    return num


def main():
    start_path = '.\\files4'
    files = [(f, start_path) for f in get_list_files(start_path)]

    with ThreadPool(5) as p:
        res = p.starmap(read_number, files)
    print(sum(res))


if __name__ == '__main__':
    main()
