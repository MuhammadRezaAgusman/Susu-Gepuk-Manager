def validasi_id(data, suggest):
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