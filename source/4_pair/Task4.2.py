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
        self.year = year

    def info(self):
        """
        Возвращает описание книги в виде строки.

        Returns:
            str: Строка с названием, автором и годом издания книги.
        """
        return f"Название: {self.title}, Автор: {self.author}, Год издания: {self.year}"

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
    
    def info(self):
        """
        Возвращает информацию об электронной книге.

        Returns:
            str: Строка с названием электронной книги, автором и годом издания.
        """
        return f"Название электронной книги: {self.title}; Автор: {self.author}; Год издания: {self.year}"


Book1 = Book("Атака на титанов г.1", "Хадзимэ Исаяма", "2009")
Ebook1 = Ebook("Что делать?", "Владимир Ильич Ульянов (Ленин)", "1902")
Ebook1.format()
print(Book1.info())
print(Ebook1.info())
