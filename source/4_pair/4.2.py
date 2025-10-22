class Book:
    def __init__(self, title, author, year):
        self.title = title
        self.author = author
        self.year = year

    def info(self):
        return f"Название: {self.title}, Автор: {self.author}, Год издания: {self.year}"

class Ebook(Book):
    def format(self):
        self.title += " (Электронный вариант)"
    def info(self):
        return f"Название электронной книги: {self.title}; Автор: {self.author}; Год издания: {self.year}"

Book1 = Book("Атака на титанов г.1", "Хадзимэ Исаяма", "2009")
Ebook1 = Ebook("Что делать?", "Владимир Ильич Ульянов (Ленин)", "1902")
Ebook1.format()
print(Book1.info())
print(Ebook1.info())