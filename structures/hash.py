class HashTable:

    def __init__(self, size):
        self.size = size
        self.table = [[] for _ in range(size)]

    def hash_function(self, telepon):

        total = 0

        for char in telepon:
            total += ord(char)

        return total % self.size

    def insert(self, telepon, data):

        index = self.hash_function(telepon)

        self.table[index].append((telepon, data))

    def search(self, telepon):

        index = self.hash_function(telepon)

        for key, value in self.table[index]:
            if key == telepon:
                return value

        return None

    def display(self):#untuk debugging aja

        for i in range(self.size):
            print(f"Bucket {i}: {self.table[i]}")