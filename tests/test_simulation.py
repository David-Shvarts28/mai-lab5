import unittest
import random
from src.simulation.simulator import (
    add_book,
    remove_item,
    try_nonexist
)
from src.classes.library import Library


class TestSimulation(unittest.TestCase):
    def setUp(self):
        self.library = Library("Тестовая библиотека")
        random.seed(42)

    def test_add_random_book(self):
        initial_len = len(self.library)
        message = add_book(self.library)
        self.assertGreater(len(self.library), initial_len)
        self.assertIn("Добавлена книга", message)

    def test_remove_random_item(self):
        add_book(self.library)
        initial_len = len(self.library)
        message = remove_item(self.library)
        self.assertLess(len(self.library), initial_len)
        self.assertIn("Удалена", message)

    def test_try_nonexistent(self):
        message = try_nonexist(self.library)
        self.assertIn("Поиск несуществующего ID", message)
        self.assertIn("не найден", message)

    def test_run_simulation_seed(self):
        random.seed(42)
        library1 = Library()
        add_book(library1)
        book1_id = list(library1.items)[0].id

        random.seed(42)
        library2 = Library()
        add_book(library2)
        book2_id = list(library2.items)[0].id

        self.assertEqual(book1_id, book2_id)


if __name__ == '__main__':
    unittest.main()
