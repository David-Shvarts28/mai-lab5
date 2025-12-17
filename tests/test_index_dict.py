import unittest
from src.collections.index_dict import IndexDict
from src.classes.book import Book


class TestIndexDict(unittest.TestCase):
    def setUp(self):
        self.index = IndexDict()
        self.book1 = Book("Война и мир", "Толстой", 1869, "Роман", "123-4567890123")
        self.book2 = Book("Анна Каренина", "Толстой", 1877, "Роман", "124-4567890124")
        self.book3 = Book("Евгений Онегин", "Пушкин", 1833, "Поэма", "125-4567890125")

    def test_append_item_id(self):
        self.index.append_item(self.book1)
        self.assertEqual(len(self.index), 1)
        self.assertEqual(self.index["123-4567890123"], self.book1)

    def test_append_item_author_index(self):
        self.index.append_item(self.book1)
        self.index.append_item(self.book2)
        books_by_author = self.index[("author", "Толстой")]
        self.assertEqual(len(books_by_author), 2)
        self.assertIn(self.book1, books_by_author)

    def test_append_item_year_index(self):
        self.index.append_item(self.book1)
        items_by_year = self.index[("year", 1869)]
        self.assertEqual(len(items_by_year), 1)
        self.assertIn(self.book1, items_by_year)

    def test_remove_item(self):
        self.index.append_item(self.book1)
        self.index.append_item(self.book2)
        self.index.remove_item(self.book1)
        self.assertEqual(len(self.index), 1)
        self.assertNotIn("123-4567890123", self.index)


if __name__ == '__main__':
    unittest.main()
