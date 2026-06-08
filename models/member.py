from utility import generate as gen
from utility import validate as vdl
from utility import file_handler as handler

class Member:
    def __init__(self, kode=None,nomor_telepon=None, nama=None, poin=None):
        self.kode = kode
        self.nomor_telepon = nomor_telepon
        self.nama = nama
        self.poin = poin
    
    def append(self):
        lib_id = handler.load_json("data_center/id_library.json")
        while True:
            self.nama = input("Masukkan Nama: ").strip()
            if vdl.validasi_nama(self.nama) == False:
                print("Nama tidak valid\n")
                continue
            break

        self.kode = gen.gen_id('member')
        lib_id['member'] = self.kode
        handler.save_json("data_center/id_library.json", lib_id)
        
        self.poin = 0

        while True:
            self.nomor_telepon = input("Masukkan Nomor Telepon: ").strip()
            if vdl.validasi_nomor_telepon(self.nomor_telepon) == False:
                print("Nomor Telepon Tidak Valid")
                continue
            break
    
    def to_dict(self):
        return {
            "nama": self.nama,
            "id": self.kode,
            "telepon": self.nomor_telepon,
            "poin": self.poin,
            "tingkat": "Reguler"
        }