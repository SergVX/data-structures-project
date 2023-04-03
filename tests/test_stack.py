"""Здесь надо написать тесты с использованием unittest для модуля stack."""
import unittest
from src import stack


class TestStack(unittest.TestCase):
    test_stack = stack.Stack()

    def test_push_to_stack(self):
        self.test_stack.push('test')
        self.assertEqual(self.test_stack.top.data, 'test')

    def test_get_el_with_pop(self):
        self.test_stack.push('data1')
        data = self.test_stack.pop()
        self.assertEqual(data, 'data1')

    def test_str(self):
        self.test_stack.push('data1')  # Добавление в стек данных
        data = self.test_stack.__str__()
        self.assertEqual(data, 'data1\ntest')


if __name__ == '__main__':
    unittest.main()
