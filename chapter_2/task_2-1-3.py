# Функция для вычисления числа Фибоначчи
import math
from concurrent.futures import ThreadPoolExecutor


def fibonacci(n):
    if n <= 1:
        return n
    return fibonacci(n - 1) + fibonacci(n - 2)


# Функция для вычисления суммы квадратных корней чисел в диапазоне
def sum_of_square_roots(start, end):
    if start == end:
        return math.sqrt(start)
    return math.sqrt(start) + sum_of_square_roots(start + 1, end)


# Функция для вычисления факториала числа
def factorial(n):
    if n == 0:
        return 1
    return n * factorial(n - 1)


def main():
    # Создайте пул потоков
    with ThreadPoolExecutor(max_workers=10) as executor:
        # Отправка задач в пул потоков
        fib_future = executor.submit(fibonacci, 20)  # Например, вычисляем 20-е число Фибоначчи
        sqrt_future = executor.submit(sum_of_square_roots, 1, 50)  # Сумма квадратных корней чисел от 1 до 50
        fact_future = executor.submit(factorial, 20)  # Факториал числа 20

        # Получение и вывод результатов задач
        fib_result = fib_future.result()
        sqrt_result = sqrt_future.result()
        fact_result = fact_future.result()

        print(f"20-е число Фибоначчи: {fib_result}")
        print(f"Сумма квадратных корней чисел от 1 до 50: {sqrt_result:.4f}")
        print(f"Факториал числа 20: {fact_result}")


if __name__ == "__main__":
    main()
