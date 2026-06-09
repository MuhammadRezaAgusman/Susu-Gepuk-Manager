class Node:
    def __init__(self, data):
        self.data = data
        self.prev = None
        self.next = None


class DoublyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def append(self, data):

        new_node = Node(data)

        if self.head is None:
            self.head = new_node
            self.tail = new_node
            return

        self.tail.next = new_node
        new_node.prev = self.tail
        self.tail = new_node

    def display_forward(self):

        current = self.head

        while current is not None:
            print(current.data)
            current = current.next

    def display_backward(self):

        current = self.tail

        while current is not None:
            print(current.data)
            current = current.prev