import os
import pathlib
from multiprocessing import Pool


def get_list_files(directory: str) -> list:
    files = [f.resolve() for f in pathlib.Path(directory).iterdir() if f.is_file()]
    return files


def read_number(file: str, start_path: str) -> int:
    try:
        with open(file, 'r', encoding='utf-8') as f:
            path = start_path + os.sep + f.readline()
    except Exception as e:
        print(e)

    try:
        with open(path, 'r', encoding='utf-8') as fl:
            num = fl.readline()
    except Exception as e:
        print(e)

    return int(num)


def main():
    start_path = '.\\files4'
    files = [(f, start_path) for f in get_list_files(start_path)]

    with Pool(5) as p:
        res = p.starmap(read_number, files)
    print(sum(res))


if __name__ == '__main__':
    main()
