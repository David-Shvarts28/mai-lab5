import random
from src.classes.library import Library
from src.classes.book import Book
from src.classes.magazine import Magazine

def gen_book() -> Book:
    '''
    Генерирует случайную книгу
    :return: случайная книга
    '''
    titles = ["Война и мир", "Преступление и наказание", "Капитанская дочка",
              "Евгений Онегин", "Мастер и Маргарита", "Отцы и дети", "Ведьмак"]
    authors = ["Толстой", "Достоевский", "Пушкин", "Булгаков", "Тургенев", "Сапковский"]
    genres = ["Роман", "Поэма", "Повесть", "Драма"]

    return Book(
        title=random.choice(titles),
        author=random.choice(authors),
        year=random.randint(1800, 2025),
        genre=random.choice(genres),
        isbn=f"{random.randint(100, 999)}-{random.randint(10000000, 99999999)}"
    )


def gen_magazine() -> Magazine:
    '''
    Генерирует случайный журнал
    :return: случайный журнал
    '''
    titles = ["IT-центр МАИ", "Playboy", "Техника",
              "National Geographic", "Forbes"]
    publishers = ["МАИ", "АСТ", "PLBY Group"]
    themes = ["Образование", "Путешествия", "Технологии", "Природа", "Бизнес", "IT", "Развлечения"]

    return Magazine(
        title=random.choice(titles),
        year=random.randint(1800, 2025),
        issue=random.randint(1, 15),
        theme=random.choice(themes),
        publisher=random.choice(publishers),
        issn=f"{random.randint(1000, 9999)}-{random.randint(10000000, 99999999)}"
    )


def add_book(library: Library) -> str:
    '''
    Добавляет случайную книгу в библиотеку
    :param library: библиотека
    :return: сообщение о добавлении книги
    '''
    book = gen_book()
    library.append_item(book)
    return f"Добавлена книга: '{book.title}' (ISBN: {book.id})"


def add_magazine(library: Library) -> str:
    '''
    Добавляет случайный журнал в библиотеку
    :param library: библиотека
    :return: сообщение о добавлении журнала
    '''
    magazine = gen_magazine()
    library.append_item(magazine)
    return f"Добавлен журнал: '{magazine.title}' №{magazine.issue}"


def remove_item(library: Library) -> str:
    '''
    Удаляет случайный элемент из библиотеки
    :param library: библиотека
    :return: сообщение об удалении элемента
    '''
    if len(library) == 0:
        return "Нечего удалять - библиотека пуста"
    item = random.choice(library.items)
    library.remove_item(item)
    item_type = "книга" if isinstance(item, Book) else "журнал"
    return f"Удалена {item_type}: '{getattr(item, 'title', 'без названия')}'"


def search_author(library: Library) -> str:
    '''
    Выполняет поиск книг по случайному автору
    :param library: библиотека
    :return: сообщение о результатах поиска
    '''
    authors = ["Толстой", "Достоевский", "Пушкин", "Клайн", "Сапковский", "Тургенев"]
    author = random.choice(authors)
    books = library.find_author(author)
    return f"Поиск автора '{author}': найдено {len(books)} книг"


def search_year(library: Library) -> str:
    '''
    Выполняет поиск элементов по случайному году
    :param library: библиотека
    :return: сообщение о результатах поиска
    '''
    years = [1800, 1880, 1900, 1950, 1978, 2006, 2012, 2025]
    year = random.choice(years)
    items = library.find_year(year)
    return f"Поиск года {year}: найдено {len(items)} элементов"


def search_genre(library: Library) -> str:
    '''
    Выполняет поиск книг по случайному жанру
    :param library: библиотека
    :return: сообщение о результатах поиска
    '''
    genres = ["Роман", "Поэма", "Повесть", "Драма", "Комедия", "Фэнтези"]
    genre = random.choice(genres)
    k = 0
    for i in library.items:
        if isinstance(i, Book) and hasattr(i, 'genre'):
            if i.genre == genre:
                k += 1

    return f"Поиск жанра '{genre}': найдено {k} книг"


def update_index(library: Library) -> str:
    '''
    Обновляет информацию об индексах библиотеки
    :param library: библиотека
    :return: сообщение о состоянии индексов
    '''
    if len(library) == 0:
        return "Обновление индекса: библиотека пуста"
    authors = len(library.index.author)
    years = len(library.index.year)
    return f"Обновление индекса: {authors} авторов, {years} по годам"


def check_item(library: Library) -> str:
    '''
    Проверяет наличие элемента в библиотеке
    :param library: библиотека
    :return: сообщение о результате проверки
    '''
    if len(library) == 0:
        return "Проверка наличия: пусто"

    if random.random() < 0.7 and len(library) > 0:
        item = random.choice(library.items)
        ex = item.id in library
        return f"Проверка ID '{item.id}': {'есть' if ex else 'нет'}"
    else:
        fake_id = f"FAKE-{random.randint(1000, 9999)}"
        ex = fake_id in library
        return f"Проверка ID '{fake_id}': {'есть' if ex else 'нет'}"


def try_nonexist(library: Library) -> str:
    '''
    Пытается найти несуществующий элемент
    :param library: библиотека
    :return: сообщение о результате поиска
    '''
    fk = f"NONE-{random.randint(1000, 9999)}"
    try:
        item = library.find_id(fk)
        stat = "найден (ошибка!)" if item else "не найден"
    except KeyError:
        stat = "не найден"
    return f"Поиск несуществующего ID '{fk}': {stat}"

def share_check(library: Library) -> str:
    '''
    Используется для воспроизведения бага с изменяемым значением в BookCollection.
    :param library: библиотека
    :return: сообщение о результате поиска
    '''
    other = Library("Другая библиотека")
    return f"Проверка: текущая={len(library)}, новая={len(other)}"


def year_index(library: Library) -> str:
    '''
    Используется для воспроизведения бага: year не очищается при удалении.
    :param library: библиотека
    :return: сообщение о результате поиска
    '''
    if len(library) == 0:
        return "Проверка: библиотека пуста"
    item = random.choice(library.items)
    year = getattr(item, "year", None)
    library.remove_item(item)
    if year is None:
        return "Проверка: у элемента нет year"
    start = len(library.find_year(year))
    return f"Проверка после удаления: год={year}, найдено={start}"


def miss_id(library: Library) -> str:
    '''
    Используется для воспроизведения бага: перехват исключения приводит к ошибке.
    :param library: библиотека
    :return: сообщение о результате поиска
    '''
    fk = f"CRASH-{random.randint(1000, 9999)}"
    item = library.find_id(fk) # при баге вернётся None
    return f"Найдено: {item.title}"


def run_simulation(steps: int = 20, seed: int | None = None) -> None:
    '''
    Запускает псевдослучайную симуляцию работы библиотеки
    :param steps: количество шагов симуляции
    :param seed: параметр для генерации случайных чисел
    '''
    if seed is not None:
        random.seed(seed)

    library = Library("Библиотека")

    all_mp = [
        add_book,
        add_magazine,
        remove_item,
        search_author,
        search_year,
        search_genre,
        update_index,
        check_item,
        try_nonexist,
        share_check,
        year_index,
        miss_id,
    ]

    #BUG №2: ошибĸа границы циĸла (off-by-one)
    # при steps=1 выполняется 2 шага (на 1 больше)
    for i in range(steps + 1):
        mp = random.choice(all_mp)
        message = mp(library)
        print(f"[Шаг {i+1}] {message}")
