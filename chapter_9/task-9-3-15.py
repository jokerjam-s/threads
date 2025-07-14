from multiprocessing.pool import ThreadPool

numbers = [6, 1, 8, 11, 4, 7, 5, 2, 3, 9]


def is_prime(n):
    if n <= 1:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    for i in range(3, int(n ** 0.5) + 1, 2):
        if n % i == 0:
            return False
    return True


def check_primes(numbers):
    pool = ThreadPool(4)
    for n in numbers:
        result = pool.apply(is_prime, args=(n,))
        print(result)
    pool.close()
    pool.join()


if __name__ == '__main__':
    check_primes(numbers)
