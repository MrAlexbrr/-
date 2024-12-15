import doctest


class Cup:
    def __init__(self, capacity_volume: float, occupied_volume: float):
        """
        Создание и подготовка к работе объекта "Кружка".

        :param capacity_volume: Объем кружки.
        :param occupied_volume: Объем занимаемой жидкости.

        Примеры:
        >>> cup = Cup(300, 0)  # инициализация экземпляра класса
        """
        if not isinstance(capacity_volume, (int, float)):
            raise TypeError("Объем кружки должен быть типа int или float")
        if capacity_volume <= 0:
            raise ValueError("Объем кружки должен быть положительным числом")
        self.capacity_volume = capacity_volume

        if not isinstance(occupied_volume, (int, float)):
            raise TypeError("Количество жидкости должно быть типа int или float")
        if occupied_volume < 0:
            raise ValueError("Количество жидкости не может быть отрицательным числом")
        if occupied_volume > capacity_volume:
            raise ValueError("Количество жидкости не может превышать объем кружки")
        self.occupied_volume = occupied_volume

    def add_liquid(self, liquid_volume: float) -> None:
        """
        Добавление жидкости в кружку.

        :param liquid_volume: Объем добавляемой жидкости.
        :raise ValueError: Если добавляемая жидкость превышает свободное место в кружке.

        Примеры:
        >>> cup = Cup(300, 100)
        >>> cup.add_liquid(150)
        """
        if liquid_volume < 0:
            raise ValueError("Объем добавляемой жидкости должен быть положительным числом")
        if self.occupied_volume + liquid_volume > self.capacity_volume:
            raise ValueError("Добавляемая жидкость превышает свободное место в кружке")
        self.occupied_volume += liquid_volume

    def remove_liquid(self, liquid_volume: float) -> None:
        """
        Удаление жидкости из кружки.

        :param liquid_volume: Объем извлекаемой жидкости.
        :raise ValueError: Если удаляемая жидкость больше текущего объема жидкости в кружке.

        Примеры:
        >>> cup = Cup(300, 200)
        >>> cup.remove_liquid(100)
        """
        if liquid_volume < 0:
            raise ValueError("Объем удаляемой жидкости должен быть положительным числом")
        if liquid_volume > self.occupied_volume:
            raise ValueError("Удаляемая жидкость превышает текущий объем")
        self.occupied_volume -= liquid_volume


class Book:
    def __init__(self, title: str, author: str, pages: int):
        """
        Создание и подготовка к работе объекта "Книга".

        :param title: Название книги.
        :param author: Автор книги.
        :param pages: Количество страниц (должно быть больше нуля).

        Примеры:
        >>> book = Book("Война и мир", "Л. Толстой", 1225)  # инициализация экземпляра класса
        """
        if not isinstance(pages, int) or pages <= 0:
            raise ValueError("Количество страниц должно быть положительным целым числом")
        self.title = title
        self.author = author
        self.pages = pages

    def read(self, pages_to_read: int) -> None:
        """
        Симулировать чтение книги.

        :param pages_to_read: Количество страниц для чтения.
        :raise ValueError: Если указанное количество страниц превышает общее количество страниц.

        Примеры:
        >>> book = Book("Гарри Поттер", "Дж. Роулинг", 500)
        >>> book.read(50)
        """
        if pages_to_read < 0:
            raise ValueError("Количество читаемых страниц должно быть положительным числом")
        if pages_to_read > self.pages:
            raise ValueError("Количество читаемых страниц превышает общее количество")
        self.pages -= pages_to_read

    def bookmark(self, page: int) -> None:
        """
        Поставить закладку на определенную страницу.

        :param page: Номер страницы для закладки.
        :raise ValueError: Если номер страницы выходит за диапазон страниц книги.

        Примеры:
        >>> book = Book("Капитанская дочка", "А. Пушкин", 150)
        >>> book.bookmark(45)
        """
        if page < 1 or page > self.pages:
            raise ValueError("Номер страницы должен быть в пределах книги")


class Smartphone:
    def __init__(self, brand: str, battery_level: float):
        """
        Создание и подготовка к работе объекта "Смартфон".

        :param brand: Название бренда смартфона.
        :param battery_level: Уровень заряда батареи (в процентах).

        Примеры:
        >>> phone = Smartphone("Apple", 100)  # инициализация экземпляра класса
        """
        if not (0 <= battery_level <= 100):
            raise ValueError("Уровень заряда должен быть от 0 до 100")
        self.brand = brand
        self.battery_level = battery_level

    def charge(self, amount: float) -> None:
        """
        Зарядка смартфона.

        :param amount: Объем заряда в процентах.
        :raise ValueError: Если уровень заряда превышает 100%.

        Примеры:
        >>> phone = Smartphone("Samsung", 50)
        >>> phone.charge(30)
        """
        if amount < 0:
            raise ValueError("Объем заряда должен быть положительным числом")
        if self.battery_level + amount > 100:
            raise ValueError("Уровень заряда не может превышать 100%")
        self.battery_level += amount

    def use(self, usage: float) -> None:
        """
        Использование смартфона, уменьшающее заряд.

        :param usage: Объем использования заряда в процентах.
        :raise ValueError: Если уровень использования превышает текущий заряд.

        Примеры:
        >>> phone = Smartphone("Xiaomi", 70)
        >>> phone.use(20)
        """
        if usage < 0:
            raise ValueError("Объем использования должен быть положительным числом")
        if usage > self.battery_level:
            raise ValueError("Уровень использования превышает текущий заряд")
        self.battery_level -= usage


if __name__ == "__main__":
    doctest.testmod(verbose=True)  # тестирование примеров, которые находятся в документации
