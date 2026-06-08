from utility import file_handler as handler

def validasi_id(data, suggest):
    if suggest == '':
        return False
    for i in range(len(data)):
        if suggest in data[i]['id'] :
            return True
    return False

def validasi_stok(data):
    if data['stok']==0:
                status = "Tidak Tersedia"
    elif data['stok'] <5 and data['stok']>0:
                status = "Stok Hampir Habis"
    elif data['stok'] >5:
                status = "Tersedia"
    return status

def validasi_nama(nama):
    if nama == '':
        return False
    elif nama.isdigit():
        return False
    elif not all(char.isalpha() or char.isspace() for char in nama):
        return False
    return True

def validasi_menu(menu_suggest):
    if menu_suggest == '':
        return False
    data_menu = handler.load_json("data_center/produk.json")
    for i in range(len(data_menu)):
        if menu_suggest in data_menu[i]['nama']:
            return True
    return False

def cek_stok(data, id, jumlah):
    for i in range(len(data)):
        if id in data[i]['kode']:
            if data[i]['stok'] < jumlah:
                return False
            else: return True  

def validasi_gerobak(nama):
    data_gerobak = handler.load_json("data_center/cabang.json")
    for i in range(len(data_gerobak)):
        if nama in data_gerobak[i]['nama']:
            return [data_gerobak[i]['nama'], data_gerobak[i]['id']] 
    else:  
        return False

def validasi_status_gerobak(data_gerobak, nama_gerobak):
    for i in range(len(data_gerobak)):
        if nama_gerobak in data_gerobak[i]['nama']:
            if data_gerobak[i]['status'] != 'BUKA':
                 return False
    return True

def validasi_nomor_telepon(nomor):
    if nomor == '':
        return False
    elif len(nomor) < 10 or len(nomor) > 15:
        return False
    elif not all(char.isdigit() for char in nomor):
        return False
    return True