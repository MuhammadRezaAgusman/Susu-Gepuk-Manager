from utility import generate as gen

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

    def lihat_member(self):

        if self.head is None:
            print("Data kosong")
            return

        current = self.head

        while True:

            nomor_telepon = gen.format_telepon(current.data['telepon'])

            print("-" * 50)
            print(f"""
[{current.data['id']}]
Nama       : {current.data['nama']}
No. Telepon: {nomor_telepon}
Poin       : {current.data['poin']}
Level      : {current.data['tingkat']}
""")

            pilihan = input(
            "[N] Next | [K] Kembali : ").upper()

            if pilihan == "N":
                current = current.next

            elif pilihan == "K":
                break

            else:
                print("Pilihan tidak valid")