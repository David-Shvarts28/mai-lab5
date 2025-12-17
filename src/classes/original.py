class Item:
    '''
    Основной класс для элементов библиотеки
    :param item_id: идентификатор элемента
    '''
    def __init__(self, item_id: str):
        self.id = item_id

    def __repr__(self):
        return f"Item(id={self.id})"
