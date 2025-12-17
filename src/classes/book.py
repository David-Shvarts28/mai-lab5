from src.classes.original import Item

class Book(Item):
    '''
    Класс, представляющий книгу в библиотеке
    :param title: название
    :param author: автор
    :param year: год издания
    :param genre: жанр
    :param isbn: ISBN
    '''
    def __init__(self, title: str, author: str, year: int, genre: str, isbn: str):
        super().__init__(isbn)
        self.title = title
        self.author = author
        self.year = year
        self.genre = genre

    def __repr__(self):
        return f"Book(title = '{self.title}', author = {self.author}, year = {self.year}, genre = {self.genre}, \
                isbn = {self.id})"
