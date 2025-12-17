class BookCollection:
    '''
    Пользовательсĸая списĸовая ĸоллеĸция для хранения книг и журналов
    '''
    def __init__(self):
        self.items = []

    def __getitem__(self, key):
        return self.items[key]

    def __iter__(self):
        return iter(self.items)

    def __len__(self):
        return len(self.items)

    def __contains__(self, key):
        if isinstance(key, str):
            for item in self.items:
                if hasattr(item, 'title') and item.title.lower() == key.lower():
                    return True
            return False
        else:
            return key in self.items

    def append(self, item) -> None:
        '''
        Добавляет элемент в коллекцию
        :param item: элемент
        '''
        self.items.append(item)

    def remove(self, item) -> None:
        '''
        Удаляет элемент из коллекции
        :param item: элемент
        '''
        self.items.remove(item)
