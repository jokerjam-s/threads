from queue import Queue
from threading import Thread

q_words = Queue()
q_lines = Queue()

# Укажите количество слов в файлах
word_count = 0

# Укажите количество строк в файлах
number_of_lines = 0


def calc_words():
    global word_count

    while not q_words.empty():
        file_name = q_words.get()
        with open(file_name) as f:
            for line in f:
                word_count += len(line.split())
        q_words.task_done()


def calc_lines():
    global number_of_lines

    while not q_lines.empty():
        file_name = q_lines.get()
        with open(file_name) as f:
            for line in f:
                number_of_lines += 1
        q_lines.task_done()


def main():
    global word_count
    word_count = 0
    for i in range(1, 4):
        q_words.put(f'file{i}.txt')
        q_lines.put(f'file{i}.txt')

    th_1 = Thread(target=calc_words)
    th_2 = Thread(target=calc_lines)

    th_1.start()
    th_2.start()

    q_words.join()
    q_lines.join()

    print(word_count)
    print(number_of_lines)


if __name__ == '__main__':
    main()
