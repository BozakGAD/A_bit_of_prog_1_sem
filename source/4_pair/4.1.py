class Book:
    def __init__(self, title, author, year):
        self.title = title
        self.author = author
        self.year = year

    def description(self):
        return f"Название: {self.title}; Автор: {self.author}; Год издания: {self.year}."

Book1 = Book("Атака на титанов т.1", "Хадзимэ Исаяма", "2009")
print(Book1.description())