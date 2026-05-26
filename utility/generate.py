def gen_id(data):
    id_terakhir = data[len(data)-1]['kode']
    id_baru= "PRD-"+str(int(id_terakhir[-4:])+1)
    return id_baru