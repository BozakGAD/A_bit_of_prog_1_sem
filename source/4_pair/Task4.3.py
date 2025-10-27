from datetime import datetime

class Book:
    """
    Класс, представляющий книгу.

    Attributes:
        title (str): Название книги.
        author (str): Автор книги.
        year (str): Год издания книги.
    """
    def __init__(self, title, author, year):
        """
        Инициализирует объект Book с указанными параметрами.

        Args:
            title (str): Название книги.
            author (str): Автор книги.
            year (str): Год издания книги.
        """
        self.title = title
        self.author = author
        self.year = int(year)

    def info(self):
        """
        Возвращает описание книги в виде строки.

        Returns:
            str: Строка с названием, автором и годом издания книги.
        """
        return f"Название: {self.title}; Автор: {self.author}; Год издания: {self.year}"

    @classmethod
    def from_str(cls, string):
        """
        Создаёт экземпляр класса Book из строки с разделителем "/".

        Args:
            string (str): Строка формата "Название/Автор/Год".

        Returns:
            Book: Новый экземпляр класса Book, созданный из строки.
        """
        title, author, year = string.split("/")
        return cls(title, author, year)

    @property
    def age(self):
        """
        Вычисляет возраст книги в годах относительно текущего года.

        Returns:
            int: Возраст книги.
        """
        return datetime.now().year - self.year

    def __str__(self):
        """
        Возвращает строковое представление объекта Book.

        Returns:
            str: Строка с основной информацией о книге.
        """
        return self.info()

    def __eq__(self, other):
        """
        Сравнивает две книги по автору.

        Args:
            other (Book): Объект, с которым производится сравнение.

        Returns:
            bool: True, если авторы совпадают, иначе False.
        """
        return self.author == other.author

class Ebook(Book):
    """
    Подкласс Book, представляющий электронную версию книги.
    Наследует все атрибуты и методы класса Book.
    """
    def format(self):
        """
        Добавляет пометку "(Электронный вариант)" к названию книги.
        """
        self.title += " (Электронный вариант)"
        self.title += " (Электронный вариант)"

    def info(self):
        """
        Возвращает информацию об электронной книге.

        Returns:
            str: Строка с названием электронной книги, автором и годом издания.
        """
        return f"Название электронной книги: {self.title}; Автор: {self.author}; Год издания: {self.year}"


Book1 = Book("Атака на титанов г.1", "Хадзимэ Исаяма", "2009")
Ebook1 = Ebook("Что делать?", "Владимир Ильич Ульянов (Ленин)", "1902")
Ebook2 = Ebook.from_str("За Волгой для нас земли не было/Василий Григорьевич Зайцев/1971")
print(Book1)
print(Ebook1)
print(Ebook2)
print(Book1 == Ebook1)

