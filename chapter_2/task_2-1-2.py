from concurrent.futures import ThreadPoolExecutor


# Функция для вычисления суммы чисел в заданном диапазоне
def sum_range(start, end):
    return sum(range(start, end + 1))


def main():
    # Создание пула потоков
    with ThreadPoolExecutor(max_workers=3) as executor:
        # Отправьте задачи в пул потоков с помощью .submit()
        proc1 = executor.submit(sum_range, 1, 100)
        proc2 = executor.submit(sum_range, 101, 200)
        proc3 = executor.submit(sum_range, 201, 300)

        sum1 = proc1.result()
        sum2 = proc2.result()
        sum3 = proc3.result()

    # Получите вывод результатов задач с помощью .result()

    print(f"Сумма чисел от 1 до 100: {sum1}")
    print(f"Сумма чисел от 101 до 200: {sum2}")
    print(f"Сумма чисел от 201 до 300: {sum3}")


if __name__ == "__main__":
    main()
