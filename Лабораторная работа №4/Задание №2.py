import json
# Решение задачи
def task() -> float:
    # Чтение данных из файла
    with open('input.json', 'r') as file:
        data = json.load(file)

    # Вычисление суммы произведений
    total_sum = sum(item["score"] * item["weight"] for item in data)

    # Округление результата до 3 знаков после запятой
    return round(total_sum, 3)


# Печать результата
print(task())
