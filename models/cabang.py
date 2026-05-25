class Cabang:
    def __init__(self, id, nama, kecamatan,):
        self.id = id
        self.nama = nama
        self.kecamatan = kecamatan
        self.penjualan = 0

    def to_dict(self):
        return {
            "id": self.id,
            "nama": self.nama,
            "kecamatan": self.kecamatan,
            "penjualan": self.penjualan
        }

