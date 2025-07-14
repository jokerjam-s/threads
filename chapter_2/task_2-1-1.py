from concurrent.futures import ThreadPoolExecutor

strings = [
    "Да Здравствует ThreadPoolExecutor!!!",
    "Многопоточность в Python позволяет выполнять несколько задач одновременно, улучшая производительность.",
    "Многопоточность может увеличить сложность управления памятью и ресурсами.",
    "Правильное использование многопоточности в Python может значительно улучшить производительность приложений."
]


def to_uppercase(message: str):
    print(message.upper())


def main():
    with ThreadPoolExecutor(max_workers=3) as executor:
        for string_val in strings:
            executor.submit(to_uppercase, string_val)


if __name__ == '__main__':
    main()
