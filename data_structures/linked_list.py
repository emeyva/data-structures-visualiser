""" Linked-list"""

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def add(self, data):
        """Add node to linked list"""
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node
    
    def delete(self, data):
        """Delete node from linked list"""
        if not self.head: 
            return "linked-list is empty"
        
        if self.head.data == data:
            self.head = self.head.next

        current = self.head
        while current.next:
            if current.next.data == data:
                current.next = current.next.next
            current = current.next

    def to_list(self):
        """Convert the linked list to a list of dictionaries."""
        elements = []
        current = self.head
        while current:
            elements.append({'data': current.data})
            current = current.next
        return elements

    def __str__(self):
        current = self.head
        values = []
        while current:
            values.append(str(current.data))
            current = current.next
        return ' -> '.join(values)
