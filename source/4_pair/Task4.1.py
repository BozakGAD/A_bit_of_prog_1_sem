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

    def description(self):
        """
        Возвращает описание книги в виде строки.

        Returns:
            str: Строка с названием, автором и годом издания книги.
        """
        return f"Название: {self.title}; Автор: {self.author}; Год издания: {self.year}."


Book1 = Book("Атака на титанов г.1", "Хадзимэ Исаяма", "2009")
print(Book1.description())

