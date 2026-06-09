class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class CircularLinkedList:
    def __init__(self):
        self.head = None

    def append(self, data):

        new_node = Node(data)

        if self.head is None:
            self.head = new_node
            new_node.next = self.head
            return

        current = self.head

        while current.next != self.head:
            current = current.next

        current.next = new_node
        new_node.next = self.head

    def display(self):

        if self.head is None:
            print("Data kosong")
            return

        current = self.head

        while True:

            print(current.data["nama"])

            current = current.next

            if current == self.head:
                break