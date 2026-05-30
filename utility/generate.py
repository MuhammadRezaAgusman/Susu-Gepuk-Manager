from utility import file_handler as handler
from utility import searching as src

def gen_id(data):
    data_id = handler.load_json("data_center/id_library.json")
    id_terakhir = int(data_id[data][-3:])+1
    id_baru= f"{data_id[data][:3]}-{id_terakhir:03}"
    data_id[data] = id_baru
    handler.save_json("data_center/id_library.json", data_id)
    return id_baru

def gen_tampilan_pesanan(data , antrean, id_antrean):
    total_harga = 0
    print(f"""          [{id_antrean}]
          nama   : {antrean['nama']}
          gerobak: {antrean['kode gerobak']}{antrean['nama gerobak']}
          pesanan: """)
    for i in range(len(antrean['pesanan'])):
        nama, harga = src.cari_detail_menu(data, antrean['pesanan'][i][0])
        total_harga += harga*antrean['pesanan'][i][1]
        print(f"        {antrean['pesanan'][i][1]}x {nama} ")
    print(f"Total Harga: Rp. {total_harga}")
    