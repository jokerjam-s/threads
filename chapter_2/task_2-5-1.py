# Полные списки вшиты в задачу
from concurrent.futures import ThreadPoolExecutor

bases = [3, 44, 22]
exponents = [12, 31, 5]


def power(base, exponent):
    return base ** exponent


def main():
    with ThreadPoolExecutor(max_workers=5) as executor:
        results = executor.map(lambda p: power(*p), zip(bases, exponents))

        for val in list(zip(results, bases, exponents)):
            result, base, exponent = val
            print(f"{base} в степени {exponent} равно {result}")


if __name__ == '__main__':
    main()
