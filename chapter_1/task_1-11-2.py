import threading

astronauts = ["Алексей Леонов", "Юрий Гагарин", "Джон Гленн"]
tasks = ["Ремонт оборудования", "Проведение экспериментов", "Мониторинг систем"]
intervals = [0.7, 1.3, 1.8]

def work(astronaut, task):
    print(f'{astronaut} выполняет задачу: {task}')

def main():
    for i in range (len(astronauts)):
        threading.Timer(intervals[i], work, (astronauts[i], tasks[i])).start()

if __name__ == '__main__':
    main()