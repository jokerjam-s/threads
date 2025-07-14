import numbers
from concurrent.futures import ThreadPoolExecutor

list1 = [16, 10]
list2 = [0, 7]
list3 = [8, 19]
list4 = [1, 20]


# Функция для вычисления произведения списка чисел и возбуждения исключения.
def multiply_numbers(numbers):
    result = 1
    for number in numbers:
        if number == 0:
            raise ValueError("Обнаружено умножение на ноль")
        result *= number
    return result


def callback_multiply(future):
    try:
        print(f'Результат: {future.result()}')
    except Exception as e:
        print(f"Обработано исключение: {future.exception()}")


def main():
    # Используйте ThreadPoolExecutor для выполнения функций
    with ThreadPoolExecutor(max_workers=10) as executor:
        for numbers in zip(list1, list2, list3, list4):
            futures = executor.submit(multiply_numbers, numbers)
            futures.add_done_callback(callback_multiply)


if __name__ == '__main__':
    main()
