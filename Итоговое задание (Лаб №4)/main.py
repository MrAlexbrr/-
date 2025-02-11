class Animal:
    """Базовый класс для всех животных."""

    def init(self, name: str, age: int):
        """
        Инициализирует объект животного.

        :param name: Имя животного
        :param age: Возраст животного
        """
        self.name = name
        self.age = age

    def make_sound(self) -> str:
        """
        Метод для издания звука.

        :return: Звук, который издаёт животное
        """
        return "Неизвестный звук"

    def str(self) -> str:
        """Возвращает строковое представление животного."""
        return f"Животное: {self.name}, Возраст: {self.age}"

    def repr(self) -> str:
        """Возвращает строку, представляющую объект в коде."""
        return f"Animal(name={self.name!r}, age={self.age})"


class Mammal(Animal):
    """Дочерний класс для млекопитающих."""

    def init(self, name: str, age: int, fur_color: str):
        """
        Инициализирует объект млекопитающего.

        :param name: Имя животного
        :param age: Возраст животного
        :param fur_color: Цвет шерсти
        """
        super().init(name, age)
        self.fur_color = fur_color

    def make_sound(self) -> str:
        """Переопределённый метод звука для млекопитающих."""
        return "Рррр!"

    def str(self) -> str:
        """Возвращает строковое представление млекопитающего."""
        return f"Млекопитающее: {self.name}, Возраст: {self.age}, Цвет шерсти: {self.fur_color}"

    def repr(self) -> str:
        """Возвращает строку, представляющую объект в коде."""
        return f"Mammal(name={self.name!r}, age={self.age}, fur_color={self.fur_color!r})"


class Bird(Animal):
    """Дочерний класс для птиц."""

    def init(self, name: str, age: int, wing_span: float):
        """
        Инициализирует объект птицы.

        :param name: Имя животного
        :param age: Возраст животного
        :param wing_span: Размах крыльев в метрах
        """
        super().init(name, age)
        self.wing_span = wing_span

    def make_sound(self) -> str:
        """Переопределённый метод звука для птиц."""
        return "Чирик-чирик!"

    def str(self) -> str:
        """Возвращает строковое представление птицы."""
        return f"Птица: {self.name}, Возраст: {self.age}, Размах крыльев: {self.wing_span} м"

    def repr(self) -> str:
        """Возвращает строку, представляющую объект в коде."""
        return f"Bird(name={self.name!r}, age={self.age}, wing_span={self.wing_span})"
