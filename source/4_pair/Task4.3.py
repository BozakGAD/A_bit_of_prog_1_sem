from datetime import datetime

class Book:
    def __init__(self, title, author, year):
        self.title = title
        self.author = author
        self.year = int(year)

    def info(self):
        return f"Название: {self.title}; Автор: {self.author}; Год издания: {self.year}"

    @classmethod
    def from_str(cls, string):
        title, author, year = string.split("/")
        return cls(title, author, year)

    @property
    def age(self):
        return datetime.now().year - self.year

    def __str__(self):
        return self.info()

    def __eq__(self, other):
        return self.author == other.author

class Ebook(Book):
    def format(self):
        self.title += " (Электронный вариант)"

    def info(self):
        return f"Название электронной книги: {self.title}; Автор: {self.author}; Год издания: {self.year}"


Book1 = Book("Атака на титанов г.1", "Хадзимэ Исаяма", "2009")
Ebook1 = Ebook("Что делать?", "Владимир Ильич Ульянов (Ленин)", "1902")
Ebook2 = Ebook.from_str("За Волгой для нас земли не было/Василий Григорьевич Зайцев/1971")
print(Book1)
print(Ebook1)
print(Ebook2)
print(Book1 == Ebook1)
