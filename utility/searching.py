from utility import validate as vdl

def cari_data_menu(nama, data):
    for i in range(len(data)):
        status = vdl.validasi_stok(data[i])
        if nama in data[i]['nama']:
            print(f"""\n[Data Ditemukan!]
            ID Produk  : {data[i]['kode']}
            Nama Varian: {data[i]['nama']}
            Harga      : Rp. {data[i]['harga']}
            Status Stok: {status}\n""")
            return
    print("Menu Tak Ditemukan")

def input_menu(data, suggest):
    for i in range(len(data)):
        if suggest in data[i]['nama']:
            return data[i]['kode']

def cari_detail_menu(data, id):
    for i in range(len(data)):
        if data[i]['kode'] == id:
            return data[i]['nama'], data[i]['harga']