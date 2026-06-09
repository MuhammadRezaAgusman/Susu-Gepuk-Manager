from utility import generate as gen

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
class LinkedList:
    def __init__(self):
        self.head = None

    def append(self, data):
        new_node = Node(data)

        if not self.head:
            self.head = new_node
            return

        current = self.head

        while current.next:
            current = current.next

        current.next = new_node
    
    def search_id(self, id):#untuk cari data gerobak
        current = self.head

        while current:

            if current.data["id"] == id:
                return current.data

            current = current.next

        return None
    
    def display(self):

        current = self.head
        if current == None:
            print("\nBelum ada member terdaftar\n")
            return
        print(f"{'ID Member'.ljust(10)} {'Nama Pelanggan'.ljust(20)} {'No. Telepon'.ljust(18)} {'Poin'.ljust(5)}")
        print('-'*65)
        count = 0
        while current is not None:
            count+=1
            nomor_telepon = gen.format_telepon(current.data['telepon'])
            print(f"{current.data['id'].ljust(10)} {current.data['nama'].ljust(20)} {nomor_telepon.ljust(18)} {str(current.data['poin']).ljust(5)} ({current.data['tingkat']})")
            current = current.next

        print("-"*65)
        print(f'Total: {count} Pelanggan Terdaftar')

