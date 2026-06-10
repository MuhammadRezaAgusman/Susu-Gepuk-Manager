from utility import file_handler as handler
from utility import searching as src
from datetime import datetime

data_produk = handler.load_json("data_center/produk.json")

def gen_id(data):
    data_id = handler.load_json("data_center/id_library.json")
    if data == 'transaksi':
        tanggal_terakhir = data_id[data][4:12]
        tanggal = datetime.now().strftime("%Y%m%d")

        if tanggal_terakhir != tanggal:
            id_baru = f"{data_id[data][:3]}-{tanggal}-001"
            data_id[data] = id_baru
            handler.save_json("data_center/id_library.json", data_id)
            return id_baru
        
        id_terakhir_diupdate = int(data_id[data][-3:])+1
        id_baru = f"{data_id[data][:3]}-{tanggal}-{id_terakhir_diupdate:03}"
        data_id[data] = id_baru
        handler.save_json("data_center/id_library.json", data_id)
        return id_baru
    
    id_terakhir_diupdate = int(data_id[data][-3:])+1
    id_baru= f"{data_id[data][:3]}-{id_terakhir_diupdate:03}"
    data_id[data] = id_baru
    handler.save_json("data_center/id_library.json", data_id)
    return id_baru

def gen_tampilan_pesanan(data , antrean, id_antrean):
    total_harga = 0
    print(f"""          [{id_antrean}]
          nama   : {antrean['nama']}
          gerobak: {antrean['kode gerobak']} {antrean['nama gerobak']}
          pesanan: """)
    for i in range(len(antrean['pesanan'])):
        nama, harga = src.cari_detail_menu(data, antrean['pesanan'][i][0])
        total_harga += harga*antrean['pesanan'][i][1]
        print(f"        {antrean['pesanan'][i][1]}x {nama}")
    print(f"Total Harga: Rp. {total_harga}")

def format_telepon(no):
    return f"{no[:4]}-{no[4:8]}-{no[8:]}"
    
def total_jual(data_cabang):
    total = 0
    for item in data_cabang:
        total += item['penjualan']
    return total

def hitung_keuntungan(data_gerobak):
    keuntungan = 2000 #keuntungan per menu
    total_keuntungan = 0
    for item in data_gerobak:
        total_keuntungan += item['penjualan']*keuntungan
    return total_keuntungan

def hitung_poin(total_harga):
    poin = total_harga // 10000
    return poin

def save_poin(data_member, nomor, jumlah):
    for i in range(len(data_member)):
        if data_member[i]['telepon'] == nomor:
            poin = hitung_poin(jumlah)
            data_member[i]['poin'] += poin
            handler.save_json("data_center/pelanggan.json", data_member)

def poin_level(poin):
    if poin < 100:
        return "Reguler"
    else: return "Premium"

def sinkronisasi_poin(data_member, nomor):
    for i in range(len(data_member)):
        if data_member[i]['telepon'] == nomor:
            status = poin_level(data_member[i]['poin'])
            data_member[i]['tingkat'] = status
            return data_member

def sinkronisasi_poin_all(data_member):
    for i in range(len(data_member)):
        status = poin_level(data_member[i]['poin'])
        data_member[i]['tingkat'] = status
        return data_member
            