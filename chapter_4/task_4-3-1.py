# Ваша задача написать программу, которая будет в многопоточном режиме обрабатывать элементы стека.
#
# Ключевые этапы:
#
# Напишите функцию, которая будет извлекать из очереди элементы в обратном порядке добавления. Во время извлечения будет выводить в консоль: Обработка элемента: <элемент>
# Создайте стек. Для добавления в него элементов используйте следующие данные:
#           data = [15, 13, 7, 19, 3, 1, 11, 5, 9, 17]
#
# Создайте и запустите 3 потока, для обработки стека.
# После обработки всех элементов очереди выведите в консоль: Все элементы успешно обработ
import queue
import threading

data = [15, 13, 7, 19, 3, 1, 11, 5, 9, 17]
lock = threading.Lock()


def th_print(message):
    with lock:
        print(message)


def process_task(item):
    th_print(f'Обработка элемента: {item}')


# Функция для извлечения элементов из стека
def process_stack(stack):
    while True:
        item = stack.get()
        process_task(item)
        stack.task_done()


def main():
    # Создание стека и добавление в него элементов
    stack = queue.LifoQueue()
    for d in data:
        stack.put(d)

    # Создание и запуск потоков для обработки стека
    for _ in range(3):
        thread = threading.Thread(target=process_stack, args=(stack,))
        thread.daemon = True
        thread.start()

    # Ожидание завершения всех потоков
    stack.join()
    print('Все элементы успешно обработаны')


if __name__ == '__main__':
    main()
