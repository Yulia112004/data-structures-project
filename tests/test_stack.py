"""Здесь надо написать тесты с использованием unittest для модуля stack."""
import unittest

from src.stack import Node, Stack

class Test_Class(unittest.TestCase):
    def test_push(self):
        stack = Stack()
        stack.push("data1")
        stack.push("data2")
        stack.push("data3")
        self.assertEqual(stack.top.data, "data3")

    def test_init_Node(self):
        n1 = Node(5, None)
        self.assertEqual(n1.data, 5)
        self.assertEqual(n1.next_node, None)

    def test_init_Stack(self):
        stack_1 = Stack()
        self.top = None
        self.assertEqual(self.top, None)

    def test_pop(self):
        stack = Stack()
        stack.push("data1")
        stack.push("data2")
        stack.push("data3")
        self.assertEqual(stack.pop(), "data3")

if __name__ == '__main__':
    unittest.main()
