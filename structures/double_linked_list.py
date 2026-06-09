from utility import searching as src

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
    
    def lihat_transaksi(self, data_produk):

        if self.head is None:
            print("Belum ada transaksi")
            return

        current = self.head

        while True:
            pesanan = set()
            for item in current.data['pesanan']:
                bucket1, bucket_dump = src.cari_detail_menu(data_produk, item[0])
                pesanan.add(bucket1)
            print("-" * 50)
            print(f"ID Transaksi      : {current.data['id transaksi']}")
            print(f"Nama Gerobak      : {current.data['nama gerobak']} [{current.data['kode gerobak']}]")
            print(f"Pelanggan         : {current.data['nama']}")
            print(f"Jenis menu pesanan: {pesanan}")
            print(f"Total             : Rp {current.data['total harga']}")

            pilihan = input("[P] Previous | [N] Next | [K] Kembali : ").upper()
            print()

            if pilihan == "N":

                if current.next is not None:
                    current = current.next
                else:
                    print("Sudah transaksi terakhir\n")

            elif pilihan == "P":

                if current.prev is not None:
                    current = current.prev
                else:
                    print("Sudah transaksi pertama\n")

            elif pilihan == "K":
                print()
                break

            else:
                print("Input tidak valid\n")