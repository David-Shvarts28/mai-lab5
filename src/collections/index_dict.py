class IndexDict:
    '''
    Пользовательская словарная коллекция для индексов элементов по ISBN, автору и году
    '''
    def __init__(self):
        self.id = {}
        self.author = {}
        self.year = {}

    def __getitem__(self, key):
        if isinstance(key, tuple) and len(key) == 2:
            index, value = key
            if index == "author":
                res = self.author.get(value, [])
                seen_ids = set()
                uni_res = []
                for item in res:
                    if item.id not in seen_ids:
                        seen_ids.add(item.id)
                        uni_res.append(item)
                return uni_res
            elif index == "year":
                res = self.year.get(value, [])
                seen_ids = set()
                uni_res = []
                for item in res:
                    if item.id not in seen_ids:
                        seen_ids.add(item.id)
                        uni_res.append(item)
                return uni_res
        if key not in self.id:
            raise KeyError(f"Ключ '{key}' не найден")
        return self.id[key]

    def __len__(self):
        return len(self.id)

    def __iter__(self):
        return iter(self.id.values())

    def __contains__(self, key):
        if isinstance(key, str):
            return key in self.id
        elif isinstance(key, tuple) and len(key) == 2:
            index, value = key
            if index == "author":
                return value in self.author and self.author[value]
            elif index == "year":
                return value in self.year and self.year[value]
        return False

    def append_item(self, item) -> None:
        '''
        Добавляет элемент в индекс и обновляет индексы
        :param item: элемент
        '''
        self.id[item.id] = item
        if hasattr(item, 'author') and item.author:
            author = item.author
            if author not in self.author:
                self.author[author] = []
            if item not in self.author[author]:
                self.author[author].append(item)

        if hasattr(item, 'year') and item.year is not None:
            year = item.year
            if year not in self.year:
                self.year[year] = []
            if item not in self.year[year]:
                self.year[year].append(item)

    def remove_item(self, item) -> None:
        '''
        Удаляет элемент из индекса и обновляет индексы
        :param item: элемент
        '''
        if item.id in self.id:
            del self.id[item.id]
        if hasattr(item, 'author') and item.author in self.author:
            if item in self.author[item.author]:
                self.author[item.author].remove(item)
                if not self.author[item.author]:
                    del self.author[item.author]
        if hasattr(item, 'year') and item.year in self.year:
            if item in self.year[item.year]:
                self.year[item.year].remove(item)
                if not self.year[item.year]:
                    del self.year[item.year]
