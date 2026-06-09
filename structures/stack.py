class Stack:
    def __init__(self):
        #menyimpan data riwayat ransaksi susu gepuk
        self.items = []

    def push(self, item):
        #memasukkan transaksi baru yang sukses ke dalam stack
        self.items.append(item)
    
    def pop(self):
        #mengambil transaksi dengan konsep LIFO
        if not self.is_empty():
            return self.items.pop()
        raise IndexError("[SIystem Status: Gagal mengambil data, stack masih kosong.]")
        
    def peek(self):
        #melihat transaksi baru tanpa menghapus
        if not self.is_empty():
            return self.items[-1]
        
    def is_empty(self):
        #memeriksa apakah riaway ada di dalam stack kosong
        return len(self.items) == 0
    
    def menampilkan_transaksi(self, limit = 3):
        #agar transaksi yang ditampilkan di menu 4 memiliki limit
        transaksi_baru = []
        total_data_transaksi = len(self.items)

        indeks_sekarang = total_data_transaksi - 1

        while indeks_sekarang >= 0 and len (transaksi_baru) < limit:
            trx = self.items[indeks_sekarang]
            transaksi_baru.append(trx)

            indeks_sekarang -= 1
        return transaksi_baru