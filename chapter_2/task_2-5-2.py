import random
from concurrent.futures import ThreadPoolExecutor

numbers = []


def generate_list():
    for num in range(150):
        numbers.append(random.randint(1, 1000))


def worker(start, end):
    global numbers

    result = []
    for num in numbers:
        if start <= num <= end:
            result.append(num)
    result.sort()
    return result


def main():
    generate_list()
    ranges = [(1, 300), (301, 500), (501, 700), (701, 999)]

    with ThreadPoolExecutor(max_workers=5) as executor:
        results = executor.map(lambda r: worker(*r), ranges)

        for i, result in enumerate(results):
            print(f"Числа в массиве от {ranges[i][0]} до {ranges[i][1]} {result}")

if __name__ == "__main__":
    main()
