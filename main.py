from abc import ABC, abstractmethod


class Table(ABC):
    """Абстрактный класс, описывающий стол."""

    def __init__(self, material: str, shape: str, legs_count: int) -> None:
        """
        Инициализация объекта стола.

        Args:
            material (str): Материал стола (должен быть непустой строкой).
            shape (str): Форма стола (должна быть непустой строкой).
            legs_count (int): Количество ножек (должно быть положительным целым числом).
        """
        if not isinstance(material, str) or not material:
            raise ValueError("Material must be a non-empty string.")
        if not isinstance(shape, str) or not shape:
            raise ValueError("Shape must be a non-empty string.")
        if not isinstance(legs_count, int) or legs_count <= 0:
            raise ValueError("Legs count must be a positive integer.")

        self.material = material
        self.shape = shape
        self.legs_count = legs_count

    @abstractmethod
    def fold(self) -> None:
        """Метод для складывания стола."""
        ...

    @abstractmethod
    def unfold(self) -> None:
        """Метод для раскладывания стола."""
        ...

    @abstractmethod
    def move(self, new_location: str) -> None:
        """Метод для перемещения стола в новую локацию."""
        ...


class Stack(ABC):
    """Абстрактный класс, описывающий стек."""

    def __init__(self, capacity: int) -> None:
        """
        Инициализация объекта стека.

        Args:
            capacity (int): Максимальная вместимость стека (должно быть положительным целым числом).
        """
        if not isinstance(capacity, int) or capacity <= 0:
            raise ValueError("Capacity must be a positive integer.")

        self.capacity = capacity
        self.stack = []

    @abstractmethod
    def push(self, item: any) -> None:
        """Метод для добавления элемента в стек."""
        ...

    @abstractmethod
    def pop(self) -> any:
        """Метод для удаления и возврата верхнего элемента стека."""
        ...

    @abstractmethod
    def peek(self) -> any:
        """Метод для просмотра верхнего элемента стека без удаления."""
        ...


class Application(ABC):
    """Абстрактный класс, описывающий приложение."""

    def __init__(self, name: str, version: str, developer: str) -> None:
        """
        Инициализация объекта приложения.

        Args:
            name (str): Название приложения (должно быть непустой строкой).
            version (str): Версия приложения (должна быть непустой строкой).
            developer (str): Разработчик приложения (должен быть непустой строкой).
        """
        if not isinstance(name, str) or not name:
            raise ValueError("Name must be a non-empty string.")
        if not isinstance(version, str) or not version:
            raise ValueError("Version must be a non-empty string.")
        if not isinstance(developer, str) or not developer:
            raise ValueError("Developer must be a non-empty string.")

        self.name = name
        self.version = version
        self.developer = developer

    @abstractmethod
    def launch(self) -> None:
        """Метод для запуска приложения."""
        ...

    @abstractmethod
    def update(self, new_version: str) -> None:
        """Метод для обновления версии приложения."""
        ...

    @abstractmethod
    def close(self) -> None:
        """Метод для закрытия приложения."""
        ...
