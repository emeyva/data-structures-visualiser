""" Linked-list"""

class Node:
    """ single units holding data and a link to the next node """
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    """ It is a collection of nodes that are linked with each other """
    def __init__(self):
        self.head = None

    def add(self, data):
        """ Method to add at the end a node with a given value """
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            return

        current_node = self.head
        while(current_node.next):
            current_node = current_node.next

        current_node.next = new_node
    
    def delete_first_node(self):
        if(self.head == None):
            return
        
        self.head = self.head.next

    def delete(self, data):
        """ Method to delete a node with a given value """
        current_node = self.head
        if not current_node: 
            return
        
        if current_node.data == data:
            self.delete_first_node()
            return

        while current_node.next:
            if current_node.next.data == data:
                current_node.next = current_node.next.next
                return
            current_node = current_node.next


    def to_list(self):
        """ Method to convert the linked list to a list of dictionaries."""
        elements = []
        current = self.head
        while current:
            elements.append(str(current.data))
            current = current.next
        return elements

    def __str__(self):
        current = self.head
        values = []
        while current:
            values.append(str(current.data))
            current = current.next
        return ' -> '.join(values)

