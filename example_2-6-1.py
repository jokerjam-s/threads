from concurrent.futures import ThreadPoolExecutor, as_completed
import time

# Функция, которая будет выполняться в каждом потоке
def task(n):
    time.sleep(n)
    return f"Задача {n} завершена"

# Создание списка задач
with ThreadPoolExecutor(max_workers=5) as executor:
    # Отправка задач в пул потоков и сохранение Future объектов
    futures = [executor.submit(task, i) for i in range(5, 0, -1)]  # Задачи с разным временем выполнения

    # Итерация по Future объектам по мере их завершения
    for future in as_completed(futures):
        # Получение и обработка результата каждой завершенной задачи
        print(future.result())