"""Здесь надо написать тесты с использованием unittest для модуля queue."""
import unittest
from src import queue


class TestQueue(unittest.TestCase):
    test_queue = queue.Queue()

    def test_enqueue(self):
        self.assertEqual(self.test_queue.head, None)
        self.test_queue.enqueue('test1')
        self.assertEqual(self.test_queue.head.data, 'test1')
        self.assertEqual(self.test_queue.tail.data, 'test1')
        self.test_queue.enqueue('test2')
        self.test_queue.enqueue('test3')
        self.assertEqual(self.test_queue.head.data, 'test1')
        self.assertEqual(self.test_queue.head.next_node.data, 'test2')
        self.assertEqual(self.test_queue.tail.data, 'test3')

    def test_str(self):
        data = self.test_queue.__str__()
        self.assertEqual(data, 'test1\ntest2\ntest3')


if __name__ == '__main__':
    unittest.main()