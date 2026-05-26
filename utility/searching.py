from utility import validate as vdl

def cari_menu(nama, data):
    for i in range(len(data)):
        status = vdl.validasi_stok(data[i])
        if nama in data[i]['nama']:
            print(f"""\n[Data Ditemukan!]
            ID Produk  : {data[i]['kode']}
            Nama Varian: {data[i]['nama']}
            Harga      : Rp. {data[i]['harga']}
            Status Stok: {status}\n""")
            return
    else: print("Menu Tak Ditemukan")

