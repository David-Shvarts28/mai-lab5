import unittest
from src.classes.book import Book
from src.classes.magazine import Magazine
from src.classes.original import Item


class TestBook(unittest.TestCase):
    def test_init(self):
        book = Book("Война и мир", "Толстой", 1869, "Роман", "123-4567890123")
        self.assertEqual(book.title, "Война и мир")
        self.assertEqual(book.author, "Толстой")
        self.assertEqual(book.year, 1869)
        self.assertEqual(book.id, "123-4567890123")

    def test_itance(self):
        book = Book("Война и мир", "Толстой", 1869, "Роман", "123-4567890123")
        self.assertIsInstance(book, Item)


class TestMagazine(unittest.TestCase):
    def test_init(self):
        magazine = Magazine("Forbes", 2020, 5, "Развлечения", "Forbes INC", "121-1212")
        self.assertEqual(magazine.title, "Forbes")
        self.assertEqual(magazine.year, 2020)
        self.assertEqual(magazine.issue, 5)
        self.assertEqual(magazine.id, "121-1212")

    def test_itance(self):
        magazine = Magazine("Forbes", 2020, 5, "Развлечения", "Forbes INC", "121-1212")
        self.assertIsInstance(magazine, Item)


if __name__ == '__main__':
    unittest.main()
