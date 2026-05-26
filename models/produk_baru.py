class Produk:
    def __init__(self, kode=None, nama=None, harga=None, stok=None):
        self.kode = kode
        self.nama = nama
        self.harga = harga
        self.stok = stok

    def insert(self, id):

        self.kode = id
        self.nama = input("Masukkan Nama Varian Baru: ")

        while True:
            try:
                self.harga = int(input("Masukkan Harga           :"))
                break
            except ValueError: print("Hanya Angka Bulat")
        
        self.stok = 0

    def to_dict(self):
        return {
            "kode": self.kode,
            "nama": self.nama,
            "harga": self.harga,
            "stok": self.stok
        }