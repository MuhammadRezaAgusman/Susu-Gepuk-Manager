import json

def load_json(path):#fungsi load data json
    with open(path, "r", encoding="utf-8") as f:
        data = json.load(f)
    return data  

def save_json(path, data): #fungsi untuk save data ke json
    with open(path, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=4)

def kurangi_stok(data_produk, id, jumlah):
    for i in range(len(data_produk)):
        if id == data_produk[i]['kode']:
            data_produk[i]['stok'] -= jumlah
    save_json("data_center/produk.json", data_produk)