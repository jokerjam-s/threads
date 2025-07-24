import pathlib
from multiprocessing import Pool


def get_list_files(directory: str) -> list:
    files = [f.resolve() for f in pathlib.Path(directory).iterdir() if f.is_file()]
    return files


def find_number(file_with_number: str, files: list) -> int:
    with open(file_with_number, 'r') as file:
        number = int(file.readline())

    counter = 0
    for file in files:
        with open(file, 'r') as f:
            numbers = [int(n) for n in f.readlines()]
        if number in numbers:
            counter += sum(numbers)
    return counter

def main():
    files_list_1 = get_list_files('.\\files5')
    files_list_2 = get_list_files('.\\files5\\folder2')

    with Pool(5) as pool:
        results = pool.starmap_async(find_number, [(file, files_list_2,) for file in files_list_1])
        print(sum(results.get()))

if __name__ == '__main__':
    main()