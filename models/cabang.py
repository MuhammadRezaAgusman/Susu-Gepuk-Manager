class Cabang:
    def __init__(self, kode, nama, kota):
        self.kode = kode
        self.nama = nama
        self.kota = kota
        self.penjualan = 0

    def to_dict(self):
        return {
            "kode": self.kode,
            "nama": self.nama,
            "kota": self.kota,
            "penjualan": self.penjualan
        }

