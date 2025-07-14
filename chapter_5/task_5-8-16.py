import threading
from time import sleep

# Словарь с именами сотрудников и временем до комнаты совещаний
# Данный словарь вшит в задачу и генерирует для каждого сотрудника случайные значения
# employee_times = {}

employee_times = {
    'Алиса': 4.44,
    'Боб': 7.33,
    'Чарли': 6.75,
}


def team_meeting(barrier, name, time_to_arrive):
    print(f'{name} начал(а) идти на совещание.')
    sleep(time_to_arrive)
    print(f'{name} прибыл(а) на совещание, затратив {time_to_arrive} секунд.')
    try:
        barrier.wait()
    except Exception as e:
        print(e)


def meet_up():
    print("Совещание началось!")


def main():
    barrier = threading.Barrier(len(employee_times), action=meet_up)

    for name, time in employee_times.items():
        threading.Thread(target=team_meeting, args=(barrier, name, time)).start()


if __name__ == '__main__':
    main()
