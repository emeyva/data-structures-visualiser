import unittest
from data_structures.linked_list import LinkedList

class TestLinkedList(unittest.TestCase):
    def test_linked_list(self):
        ll = LinkedList()
        ll.add(1)
        ll.add(2)
        ll.add(3)
        self.assertEqual(str(ll), '3 -> 2 -> 1')

if __name__ == '__main__':
    unittest.main()
