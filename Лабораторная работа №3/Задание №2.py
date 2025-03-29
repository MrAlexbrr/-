# Функция для поиска общих участников
def find_common_participants(group1, group2, separator=','):
    # Разделяем строки на списки фамилий по разделителю
    participants_group1 = set(group1.split(separator))
    participants_group2 = set(group2.split(separator))

    # Находим пересечение двух множеств (общие участники)
    common_participants = participants_group1 & participants_group2

    # Возвращаем отсортированный список общих участников
    return sorted(common_participants)


# Пример использования функции
participants_first_group = "Иванов|Петров|Сидоров"
participants_second_group = "Петров|Сидоров|Смирнов"

# Проверка работы функции с разделителем, отличным от запятой (например, '|')
common = find_common_participants(participants_first_group, participants_second_group, separator='|')

# Вывод результата
print("Общие участники:", common)
