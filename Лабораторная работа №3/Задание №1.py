# Функция для поиска индекса первого вхождения товара в списке
def find_item_index(items_list, item):
    # Проверяем, есть ли товар в списке
    if item in items_list:
        return items_list.index(item)  # Возвращаем индекс первого вхождения
    else:
        return None  # Возвращаем None, если товар не найден


# Список товаров
items_list = ['яблоко', 'банан', 'апельсин', 'груша', 'киви', 'банан']

# Поиск товаров в списке
for find_item in ['банан', 'груша', 'персик']:
    # Вызов функции для поиска индекса
    index_item = find_item_index(items_list, find_item)

    # Вывод результата
    if index_item is not None:
        print(f"Первое вхождение товара '{find_item}' имеет индекс {index_item}.")
    else:
        print(f"Товар '{find_item}' не найден в списке.")
