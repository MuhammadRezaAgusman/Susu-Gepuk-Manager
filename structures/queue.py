from utility import searching as src
class Queue:
    def __init__(self):
        self.items = []

    def enqueue(self, data):
        self.items.append(data)

    def dequeue(self):
        if not self.is_empty():
            return self.items.pop(0)

    def is_empty(self):
        return len(self.items) == 0
    
    def size(self):
        return len(self.items)

    def display(self, data_produk):
        total_harga = 0
        for i, item in enumerate(self.items, start=1):
            print(f"{i}.[{item['id antrian']}] {item['nama']} | {item['nama gerobak']}")
            for j in range(len(item['pesanan'])):
                nama, harga = src.cari_detail_menu(data_produk, item['pesanan'][j][0])
                total_harga += item['pesanan'][j][1]*harga
                print(f"   {item['pesanan'][j][1]}x {nama}")
            print(f"Total: Rp.{total_harga},00")
            print("-"*30)
        print("Total", self.size(),"Antrian")
        print()