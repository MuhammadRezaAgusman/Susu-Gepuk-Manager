class Produk:
    def __init__(self, kode, nama, harga, stok):
        self.kode = kode
        self.nama = nama
        self.harga = harga
        self.stok = stok

    def to_dict(self):
        return {
            "kode": self.kode,
            "nama": self.nama,
            "harga": self.harga,
            "stok": self.stok
        }