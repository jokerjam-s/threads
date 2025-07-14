from concurrent.futures import ThreadPoolExecutor

digits = [2, 17, 8, 11, 14, 5]

def calculate(num):
    return num * num


def main():
    results = []
    with ThreadPoolExecutor(max_workers=3) as executor:
        results = executor.map(calculate, digits)

    for result in results:
        print(result)

if __name__ == '__main__':
    main()
