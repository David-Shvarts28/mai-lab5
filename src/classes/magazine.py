from src.classes.original import Item

class Magazine(Item):
    '''
    Класс, представляющий журнал в библиотеке
    :param title: название журнала
    :param year: год издания
    :param issue: номер выпуска
    :param theme: тема журнала
    :param publisher: издательство
    :param issn: ISSN журнала
    '''
    def __init__(self, title: str, year: int, issue: int, theme: str, publisher: str, issn: str):
        super().__init__(issn)
        self.title = title
        self.year = year
        self.issue = issue
        self.theme = theme
        self.publisher = publisher

    def __repr__(self):
        return f"Magazine(title = '{self.title}', year = {self.year}, issue = {self.issue}, theme = {self.theme}, \
        publisher = {self.publisher}, issn = {self.id})"
