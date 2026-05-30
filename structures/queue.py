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

    def display(self):
        for i, item in enumerate(self.items, start=1):
            print(f"{i}. {item['nama']} | {item['nama gerobak']}\n")
            for j in range(len(item['pesanan'])):
                print(f"   {item['pesanan'][j][1]}x {item['pesanan'][j][0]}")
        print("Total", self.size(),"Antrian")