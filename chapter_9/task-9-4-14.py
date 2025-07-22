from multiprocessing.pool import Pool
import time

# Полный список вшит в задачу
users = [
       {"name": "Алиса", "age": 30, "city": "Москва"},
       {"name": "Борис", "age": 25, "city": "Санкт-Петербург"},
       ]

# Функция для обработки информации о пользователе
def process_user_info(user: dict):
    time.sleep(1)
    name, age, city = user.values()
    return f"{name}, {age} лет, из города {city}"

# Функция обратного вызова, которая будет вызвана для каждого результата
def on_user_processed(result):
    print(f"Обработанная информация о пользователе: {result}")

def main():
    pool = Pool(4)
    results = [pool.apply_async(process_user_info, args=(user,), callback=on_user_processed) for user in users]

    pool.close()
    pool.join()


if __name__ == "__main__":
    main()