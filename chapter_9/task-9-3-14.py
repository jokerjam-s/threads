from multiprocessing.pool import ThreadPool

numbers = [5, 3, 7, 11, 17, 23, 25, 29, 30]


def factorial(n):
    if n < 0:
        raise ValueError("Factorial is not defined for negative numbers.")
    elif n == 0:
        return 1
    else:
        fact = 1
        for i in range(1, n + 1):
            fact *= i
        return fact


def calculate_factorial(nums):
    pool = ThreadPool(4)
    for n in nums:
        result = pool.apply(factorial, args=(n,))
        print(result)
    pool.close()
    pool.join()


if __name__ == '__main__':
    calculate_factorial(numbers)
