class Produk:
    def __init__(self, kode=None, nama=None, harga=None,modal=None, stok=None):
        self.kode = kode
        self.nama = nama
        self.harga = harga
        self.modal = modal
        self.stok = stok

    def insert(self, id):

        self.kode = id
        self.nama = input("Masukkan Nama Varian Baru: ").strip()

        while True:
            try:
                self.harga = int(input("Masukkan Harga           : "))
                break
            except ValueError: print("Hanya Angka Bulat")
        
        self.modal = self.harga - 2000 
        self.stok = 0

    def to_dict(self):
        return {
            "kode": self.kode,
            "nama": self.nama,
            "harga": self.harga,
            "modal": self.modal,
            "stok": self.stok
        }