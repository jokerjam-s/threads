import os
from concurrent.futures import ThreadPoolExecutor, wait
from threading import Lock


def process_file(filename, lock: Lock):
    """Функция для обработки одного файла."""
    sum_ = 0
    with open(filename, 'r') as file:
        for line in file:
            # Преобразуем строку в число, умножаем на 3, делим на 4 и суммируем
            number = int(line.strip())
            sum_ += (number * 3) / 4
    # Записываем полученную сумму в итоговый файл
    lock.acquire()
    with open('result.txt', 'a', encoding='utf-8') as file:
        file.write(str(sum_)+'\n')
    lock.release()


# Допишите функцию main()
def main():
    write_lock = Lock()
    base_path = os.getcwd() + '\\data2'
    files_list = os.listdir(base_path)
    base_path += '\\'

    with ThreadPoolExecutor(max_workers=10) as executor:
        futures = [executor.submit(process_file, f'{base_path}{file}', write_lock) for file in files_list]

        wait(futures)


if __name__ == '__main__':
    main()
