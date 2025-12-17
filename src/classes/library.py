from src.collections.book_collection import BookCollection
from src.collections.index_dict import IndexDict


class Library:
    '''
    Класс, представляющий библиотеку с коллекцией книг и их индексами
    :param name: название библиотеки
    '''
    def __init__(self, name: str = "Библиотека №1"):
        self.name = name
        self.items = BookCollection()
        self.index = IndexDict()

    def __len__(self):
        return len(self.items)

    def __contains__(self, key):
        if isinstance(key, str):
            return key in self.index

        elif hasattr(key, 'id'):
            return key in self.items

        elif isinstance(key, tuple) and len(key) == 2:
            index_type, value = key
            if index_type == "author":
                books = self.find_author(value)
                return len(books) > 0

        return False

    def __repr__(self):
        return f"Library(name = '{self.name}', items={len(self.items)})"

    def append_item(self, item) -> None:
        '''
        Добавляет элемент в библиотеку и обновляет индексы
        :param item: элемент
        '''
        self.items.append(item)
        self.index.append_item(item)

    def remove_item(self, item) -> None:
        '''
        Удаляет элемент из библиотеки и обновляет индексы
        :param item: элемент
        '''
        if item in self.items:
            self.items.remove(item)
            self.index.remove_item(item)

    def find_author(self, author: str) -> list:
        '''
        Находит все книги указанного автора
        :param author: имя автора
        :return: список книг автора
        '''
        return self.index[("author", author)]

    def find_year(self, year: int) -> list:
        '''
        Находит все элементы указанного года
        :param year: год издания
        :return: список элементов
        '''
        return self.index[("year", year)]

    def find_id(self, item_id: str):
        '''
        Находит элемент по идентификатору
        :param item_id: идентификатор элемента
        :return: найденный элемент
        :raise KeyError: ошибка, если элемент не найден
        '''
        return self.index[item_id]
