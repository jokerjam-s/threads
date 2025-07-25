# Полный список вшит в задачу, вставлять его в поле ответа не нужно
orders = [{'name': 'Ivan', 'balance': 500, 'order': 'борщ', 'Стоимость блюда': 200},
          {'name': 'User5f4a', 'balance': 117, 'order': 'суп', 'Стоимость блюда': 161},
          {'name': 'User71e3', 'balance': 749, 'order': 'борщ', 'Стоимость блюда': 213},
          {'name': 'Userecf7', 'balance': 1509, 'order': 'салат', 'Стоимость блюда': 103},
          {'name': 'Usera299', 'balance': 45, 'order': 'шашлык', 'Стоимость блюда': 106},
          {'name': 'Userf4f8', 'balance': 172, 'order': 'шашлык', 'Стоимость блюда': 121},
          {'name': 'Userc6fd', 'balance': 71, 'order': 'борщ', 'Стоимость блюда': 51}]

from concurrent.futures import ThreadPoolExecutor, wait

# Функция для обработки заказа
def process_order(order: dict):
    if order['balance'] < order['Стоимость блюда']:
        raise ValueError(f"Недостаточно средств для заказа {order['order']} пользователя {order['name']}")
    else:
        return f"Заказ {order['order']} пользователя {order['name']} успешно обработан"


def main():
    # Используйте ThreadPoolExecutor для обработки заказов
    with ThreadPoolExecutor(max_workers=10) as executor:
        futures = [executor.submit(process_order, order) for order in orders]

        wait(futures)

        for future in futures:
            try:
                print(future.result())
            except ValueError as e:
                print(e)


if __name__ == '__main__':
    main()
