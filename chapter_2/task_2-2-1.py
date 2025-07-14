from concurrent.futures import ThreadPoolExecutor

list1 = ['kw63vdxI', 'YmSsWblC', '5OJ3Mto9']
list2 = ['7GBrUY6t', 'bfQjS3gj', 'MhTsKf0X']
list3 = ['mt05f80F', 'haHHiXoX', 'v2cYPhRO']

# Функция воркера, которая печатает сообщение из списка
def worker(texts, thread_num):
    for text in texts:
        print(f'Поток {thread_num} извлёк текст из списка: {text}')


def main():
    thread_list = []
    # Использование ThreadPoolExecutor для параллельного выполнения
    with ThreadPoolExecutor(max_workers=5) as executor:
        thread_list.append(executor.submit(worker, list1, 1))
        thread_list.append(executor.submit(worker, list2, 2))
        thread_list.append(executor.submit(worker, list3, 3))

        for t in thread_list:
            t.result()


if __name__ == '__main__':
    main()
