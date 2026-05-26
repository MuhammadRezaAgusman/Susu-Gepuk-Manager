from utility import file_handler as handler
from utility import searching as src
from utility import sorting as srt
from utility import validate
from utility import generate as gen
from models import cabang, pelanggan, produk_baru, transaksi
from structures import circular_linked_list, double_linked_list, graph, linked_list, queue, stack, tree
import time


def tampilkan_menu_utama():#pungsi menampilkan menu utama
    print("="*55)
    print("          S U S U   G E P U K  M A N A G E R")
    print("   - Sistem Manajemen Gerobak Susu Gepuk Pekanbaru -   ")
    print("="*55)
    time.sleep(1)
    print("[System Status: Data berhasil dimuat dari JSON]")
    print()
    time.sleep(0.5)
    print("[1] Manajemen Gerobak")
    print("[2] Menu Varian Susu Gepuk")
    print("[3] Pemesanan/Kasir Antrean")
    print("[4] Riwayat Transaksi Terakhir")
    print("[5] Data Pelanggan Terdaftar")
    print("[6] Keluar")
    print("="*55)

def tampilan_menu_1(data):#menampilkan isi menu 1
    print("-"*65)
    print("DAFTAR GEROBAK SUSU GEPUK")
    print("-"*65)
    print("ID         GEROBAK                       KECAMATAN           STATUS")
    print("-"*65)
    for i in range(len(data)):
        print(f"{data[i]["id"].ljust(11)}{data[i]["nama"].ljust(30)}{data[i]["kecamatan"].ljust(20)}{data[i]["status"].ljust(8)}")
    print("-"*65)
    print(f"[Total: {i+1} Gerobak]")
    


def tampilan_menu_2():
    print("="*55)
    print("            V A R I A N  S U S U  G E P U K")
    print("="*55)
    print()
    print("[1] Lihat Semua Menu [Urutan harga termurah - BST in-order]")
    print("[2] Cari Varian Rasa")
    print("[3] Tambah Varian Rasa Baru")
    print("[4] Kembali Ke Menu Utama")
    print()
    print("="*55)

def tampilan_menu_3():
    print("-"*55)
    print("            KASIR DAN ANTREAN PESANAN (Queue)")
    print("-"*55)
    print()
    print("[1] Tambah Pesanan Baru Ke Antrean")
    print("[2] Proses / Buat Pesanan Paling Terdepan (Dequeue)")
    print("[3] Lihat Sisa Antrean Saat Ini")
    print("[4] Kembali ")
    print()

def tampilan_menu_4():
    print("-"*55)
    print("            RIWAYAT TRANSAKSI TERAKHIR (STACK)")
    print("-"*55)

def tampilan_menu_5():#fungsi menampilkan menu 2
    print("="*55)
    print("               D A T A  P E L A N G G A N")
    print("="*55)
    print()
    print("[1] Lihat Semua Pelanggan Terdaftar")
    print("[2] Cari Data Pelanggan")
    print("[3] Registrasi Pelanggan Baru")
    print("[4] Kembali ke menu utama")
    print()
    print("="*55)
    print()

def menu_1():
    #load data cabang.json
    data_cabang = handler.load_json("data_center/cabang.json")
    tampilan_menu_1(data_cabang)

    #json ke linked list
    ll = linked_list.LinkedList()
    for cabang in data_cabang:
        ll.append(cabang)

    while True:
        print("\n>> Pilihan Fitur:")
        print("   [A] Cek Gerobak")
        print("   [B] Cek Rute Distribusi Bahan Baku")
        print("   [C] Ubah status gerobak")
        print("   [D] Kembali ke menu utama")

        pilih = input("Pilih Opsi (A/B/C): ").upper()
        if pilih == "A":
            id = input("Masukkan id gerobak: ").upper()
            hasil = ll.search_id(id)
            if hasil:
                print(f"""Gerobak ditemukan!
                Gerobak  : {hasil['nama']}
                ID       : {hasil['id']}
                Kecamatan: {hasil['kecamatan']}
                Status   : {hasil['status']}
                Penjualan: {hasil['penjualan']}""")
            else: print("Gerobak tidak ditemukan")
        elif pilih == "B":
            #load json untuk jalur graph
            data_jalur = handler.load_json("data_center/jalur.json")

            #inisiasi class untuk objek
            path = graph.Graph() 

            #buat graph
            for item in data_jalur:
                path.add_edge(
                    item['asal'],
                    item['tujuan'],
                    item['jarak']
                )

            print("\n= RUTE DISTRIBUSI TERCEPAT (Algoritma Graph) =")
            while True:
                asal = input("Masukkan ID Gerobak Asal: ").upper()
                if src.validasi_id(data_cabang, asal) == True:#validasi input id asal
                    break
                else: print("ID asal tak ditemukan")

            while True:
                tujuan = input("Masukkan ID Gerobak Tujuan: ").upper()
                if src.validasi_id(data_cabang, tujuan) == True:#validasi input id tujuan
                    break
                else: print("ID asal tak ditemukan") 

            jarak, rute = path.dijkstra(asal, tujuan)
            print("Mencari rute terpendek via Graph...")
            time.sleep(0.5)
            print("Rute ditemukan:", " -> ".join(rute))
            print("Total estimasi jarak:", jarak, "KM")

        elif pilih == "C":
            print("\nDaftar cabang: ")
            print("-"*65)
            print("ID         GEROBAK                       KECAMATAN           STATUS")
            print("-"*65)
            for i in range(len(data_cabang)):
                print(f"{data_cabang[i]["id"].ljust(11)}{data_cabang[i]["nama"].ljust(30)}{data_cabang[i]["kecamatan"].ljust(20)}{data_cabang[i]["status"].ljust(8)}")
            print("-"*65)

            while True:
                pilih_cabang = input("Masukkan ID Cabang: ").upper()

                #validasi input id cabang
                if validate.validasi_id(data_cabang, pilih_cabang) != True:
                    print("ID tidak valid")
                
                for i in range(len(data_cabang)):
                    if data_cabang[i]['id'] == pilih_cabang:
                        print(f"Gerobak ID {data_cabang[i]['nama']} Berstatus {data_cabang[i]['status']}")
                        while True:
                            status = input("Ingin ubah status? (Y/N)").upper()
                            if status == "Y":
                                if data_cabang[i]['status'] == "BUKA":
                                    data_cabang[i]['status'] = "TUTUP"
                                    print(f"Gerobak {data_cabang[i]['nama']} ({data_cabang[i]['id']}) di-{data_cabang[i]['status']}")
                                    handler.save_json("data_center/cabang.json", data_cabang)
                                    break
                                else: 
                                    data_cabang[i]['status'] == "BUKA"
                                    print(f"Gerobak {data_cabang[i]['nama']} ({data_cabang[i]['id']}) di-{data_cabang[i]['status']}")
                                    handler.save_json("data_center/cabang.json", data_cabang)
                                    break
                            elif status == "N":
                                print("Tidak ada cabang yang berubah status")
                                break
                            else: print("Masukkan Input dengan benar")
                break                
            
        elif pilih == "D": break
        else:
            print("Masukan salah")
    
def menu_2():
    #Data produk.json di-load ke sistem
    data_produk = handler.load_json("data_center/produk.json")
    while True:
        try:
            tampilan_menu_2()
            menu = int(input("Pilih Opsi (1-4): "))

            if menu == 1:                
                bst = tree.BinarySearchTree()
                for produk in data_produk:#memasukkan data produk ke binary search tree
                    bst.insert(produk)
                print("\n-------- DAFTAR MENU SUSU GEPUK PEKANBARU (Urutan Harga) --------")
                print("ID Produk".ljust(12),"Varian Rasa".ljust(28),"Harga".ljust(13),"Stok")
                print("-----------------------------------------------------------------")
                bst.inorder()
                print("-----------------------------------------------------------------")
                print("[Sistem: Data diambil melalui struktur Binary Search Tree]")
                print()
            elif menu == 2:
                print("\n== Cari Varian Rasa ==")
                varian = input("Masukkan Nama Varian: ")
                src.cari_menu(varian, data_produk)

            elif menu == 3:
                varian_baru = produk_baru.Produk()
                new_id = gen.gen_id(data_produk)
                varian_baru.insert(new_id)
                data_produk.append(varian_baru.to_dict())
                handler.save_json("data_center/produk.json", data_produk)
            elif menu == 4:
                break
            else: print("Menu tidak ada")
        except ValueError: print("\nMenu hanya berupa angka bulat")

def menu_3():
    tampilan_menu_3()
    while True:
        try:
            menu = int(input("Pilih Opsi (1-4): "))
            if menu == 1:
                pass
            elif menu == 2:
                pass
            elif menu == 3:
                pass
            elif menu == 4:
                break
            else: print("Menu tidak ada")
        except ValueError: print("\nMenu hanya berupa angka bulat")

def menu_4():
    pass

def menu_5():#fungsi untuk proses menu 5
    while True:
        try:
            tampilan_menu_5()
            menu = int(input("Pilih Opsi (1-4): "))
            if menu == 1:
                continue
            elif menu == 2:
                continue
            elif menu == 3:
                continue
            elif menu == 4:
                continue
            else: print("\nOpsi tidak ada")
        except ValueError: print("\ninput hanya berupa angka bulat\n")

def system():#fungsi sistem utama
    while True:
        try:
            tampilkan_menu_utama()
            menu = int(input("Pilih Menu (1-6): "))
            if menu == 1:
                print()
                menu_1()
            elif menu == 2:
                print()
                menu_2()
            elif menu == 3:
                print()
                menu_3()
            elif menu == 4:
                print()
                tampilan_menu_4()
            elif menu == 5:
                print()
                menu_5()
                continue
            elif menu == 6:
                print()
                print("Selesai")
                break
            else: print("\nMenu Tidak ada")
        except ValueError: print("\nMasukkan menu yang sesuai\n")              
            
system()