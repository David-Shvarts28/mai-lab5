import unittest
from src.classes.library import Library
from src.classes.book import Book


class TestLibrary(unittest.TestCase):
    def setUp(self):
        self.library = Library("Тестовая библиотека")
        self.book1 = Book("Война и мир", "Толстой", 1869, "Роман", "123-4567890123")
        self.book2 = Book("Анна Каренина", "Толстой", 1877, "Роман", "124-4567890124")
        self.book3 = Book("Евгений Онегин", "Пушкин", 1833, "Поэма", "125-4567890125")

    def test_append_item(self):
        self.library.append_item(self.book1)
        self.assertEqual(len(self.library), 1)
        self.assertEqual(len(self.library.items), 1)
        self.assertEqual(len(self.library.index), 1)

    def test_remove_item(self):
        self.library.append_item(self.book1)
        self.library.append_item(self.book2)
        self.library.remove_item(self.book1)
        self.assertEqual(len(self.library), 1)
        self.assertNotIn(self.book1, self.library.items)

    def test_find_author(self):
        self.library.append_item(self.book1)
        self.library.append_item(self.book2)
        self.library.append_item(self.book3)
        books = self.library.find_author("Толстой")
        self.assertEqual(len(books), 2)
        self.assertIn(self.book1, books)

    def test_find_year(self):
        self.library.append_item(self.book1)
        items = self.library.find_year(1869)
        self.assertEqual(len(items), 1)
        self.assertIn(self.book1, items)

    def test_find_id_not_found(self):
        with self.assertRaises(KeyError):
            self.library.find_id("nonexistent-id")

    def test_contains_id(self):
        self.library.append_item(self.book1)
        self.assertTrue("123-4567890123" in self.library)
        self.assertFalse("nonexistent-id" in self.library)


if __name__ == '__main__':
    unittest.main()
