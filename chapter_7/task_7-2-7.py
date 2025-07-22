import time
from concurrent.futures import ThreadPoolExecutor, as_completed

# Полный список вшит в задачу, вставлять его в поле ответа не требуется
lists = [
    [324, 643, 171, 208, 330, 306, 559, 927, 871, 284, 438, 644, 447, 893, 287],
    [993, 788, 192, 169, 549, 162, 324, 213, 277, 376, 391, 243, 749, 229, 545, 516, 260, 798],
    [100, 100, 100, 100],
]


# Функция для обработки числа
def process_number(number):
    time.sleep(0.2)  # Имитация задержки
    return number * 2


# Напишите ваш код ниже
def list_process(start_list):
    for i in range(len(start_list)):
        start_list[i] = process_number(start_list[i])

    return start_list


processed_lists = []
with ThreadPoolExecutor(max_workers=10) as executor:
    futures = [executor.submit(list_process, l) for l in lists]

    for future in as_completed(futures):
        processed_lists.append(future.result())

print(f"Сумма чисел в первом обработанном списке: {sum(processed_lists[0])}")
