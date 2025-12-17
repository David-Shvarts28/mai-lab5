import unittest
from src.collections.book_collection import BookCollection
from src.classes.book import Book


class TestBookCollection(unittest.TestCase):
    def setUp(self):
        self.collection = BookCollection()
        self.book1 = Book("Война и мир", "Толстой", 1869, "Роман", "123-4567890123")
        self.book2 = Book("Преступление и наказание", "Достоевский", 1866, "Роман", "124-4567890124")
        self.book3 = Book("Ведьмак", "Сапковский", 1986, "Фэнтези", "222-1232322332")

    def test_append(self):
        self.assertEqual(len(self.collection), 0)
        self.collection.append(self.book1)
        self.assertEqual(len(self.collection), 1)

    def test_remove(self):
        self.collection.append(self.book1)
        self.collection.append(self.book2)
        self.collection.remove(self.book1)
        self.assertEqual(len(self.collection), 1)
        self.assertEqual(self.collection[0], self.book2)

    def test_get_item(self):
        self.collection.append(self.book1)
        self.collection.append(self.book2)
        self.collection.append(self.book3)
        slice_result = self.collection[0:2]
        self.assertEqual(len(slice_result), 2)
        self.assertEqual(slice_result[0], self.book1)

    def test_iter(self):
        self.collection.append(self.book1)
        self.collection.append(self.book2)
        items = list(self.collection)
        self.assertEqual(len(items), 2)
        self.assertIn(self.book1, items)

    def test_contains_obj(self):
        self.collection.append(self.book1)
        self.assertTrue(self.book1 in self.collection)
        self.assertFalse(self.book2 in self.collection)


if __name__ == '__main__':
    unittest.main()
