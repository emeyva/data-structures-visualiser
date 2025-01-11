""" BinaryTree """
class Node:
    def __init__(self, key):
        self.left = None
        self.right = None
        self.value = key

class BinaryTree:
    def __init__(self):
        self.root = None

    def insert(self, key):
        if not self.root:
            self.root = Node(key)
        else:
            self._insert(self.root, key)

    def _insert(self, root, key):
        if key < root.value:
            if root.left is None:
                root.left = Node(key)
            else:
                self._insert(root.left, key)
        else:
            if root.right is None:
                root.right = Node(key)
            else:
                self._insert(root.right, key)

    def __str__(self):
        values = []
        self._in_order_traversal(self.root, values)
        return ' -> '.join(str(v) for v in values)

    def _in_order_traversal(self, node, values):
        if node:
            self._in_order_traversal(node.left, values)
            values.append(node.value)
            self._in_order_traversal(node.right, values)
