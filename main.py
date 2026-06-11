from utility import file_handler as handler
from utility import searching as src
from utility import sorting as srt
from utility import validate
from utility import generate as gen
from models import member, produk_baru
from structures import circular_linked_list, double_linked_list, graph, linked_list, queue, stack, tree, hash
import time
import datetime


data_keuangan = handler.load_json("data_center/keuangan.json")
saldo = data_keuangan['saldo']

hari = datetime.datetime.now()
hari_ini = hari.strftime("%A")


def tampilkan_menu_utama():#fungsi menampilkan menu utama
    print("="*65)
    print("          S U S U   G E P U K  M A N A G E R")
    print("   - Sistem Manajemen Gerobak Susu Gepuk Pekanbaru -   ")
    print("="*65)
    print()
    time.sleep(0.5)
    print("[1] Manajemen Gerobak")
    print("[2] Menu Varian Susu Gepuk")
    print("[3] Pemesanan/Kasir Antrean")
    print("[4] Riwayat Transaksi Terakhir")
    print("[5] Data Pelanggan Terdaftar")
    print("[6] Data Keuangan")
    print("[7] Keluar")
    print("="*65)

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
    print("="*65)
    print("            V A R I A N  S U S U  G E P U K")
    print("="*65)
    print()
    print("[1] Lihat Semua Menu [Urutan harga termurah - BST in-order]")
    print("[2] Cari Varian Rasa")
    print("[3] Tambah Varian Rasa Baru")
    print("[4] Tambah Stok")
    print("[5] Kembali Ke Menu Utama")
    print()
    print("="*65)

def tampilan_menu_3():
    print("-"*65)
    print("            KASIR DAN ANTREAN PESANAN (Queue)")
    print("-"*65)
    print()
    print("[1] Tambah Pesanan Baru Ke Antrean")
    print("[2] Proses / Buat Pesanan Paling Terdepan (Dequeue)")
    print("[3] Lihat Sisa Antrean Saat Ini")
    print("[4] Kembali ")
    print()

def tampilan_menu_4():
    print("-"*65)
    print("            RIWAYAT TRANSAKSI")
    print("-"*65)

def tampilan_menu_5():#fungsi menampilkan menu 5 
    print("="*65)
    print("               D A T A  P E L A N G G A N")
    print("="*65)
    print()
    print("[1] Lihat Semua Pelanggan Terdaftar")
    print("[2] Cari Data Pelanggan")
    print("[3] Registrasi Pelanggan Baru")
    print("[4] Lihat Pelanggan Terdaftar Satu - Satu")
    print("[5] Kembali ke menu utama")
    print()
    print("="*65)
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

        pilih = input("\nPilih Opsi (A-D): ").upper()
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
                if validate.validasi_id(data_cabang, asal) == True:#validasi input id asal
                    break
                else: 
                    print("ID asal tak ditemukan")

            while True:
                tujuan = input("Masukkan ID Gerobak Tujuan: ").upper()
                if validate.validasi_id(data_cabang, tujuan) == True:#validasi input id tujuan
                    break
                else: 
                    print("ID tujuan tak ditemukan") 

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
                    continue
                
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
                                    data_cabang[i]['status'] = "BUKA"
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
    global saldo

    #Data produk.json di-load ke sistem
    data_produk = handler.load_json("data_center/produk.json")
    bst = tree.BinarySearchTree()
    while True:
        try:
            tampilan_menu_2()
            menu = int(input("Pilih Opsi (1-4): "))

            if menu == 1:                
                for produk in data_produk:#memasukkan data produk ke binary search tree
                    bst.insert(produk)
                print("\n-------- DAFTAR MENU SUSU GEPUK PEKANBARU (Urutan Harga) --------")
                print("ID Produk".ljust(12),"Varian Rasa".ljust(28),"Harga".ljust(13),"Stok")
                print("-----------------------------------------------------------------")
                bst.inorder()
                print("-----------------------------------------------------------------")
                print("[System Status: Data diambil melalui struktur Binary Search Tree]")
                print()
            elif menu == 2:
                print("\n== Cari Varian Rasa ==")
                varian = input("Masukkan Nama Varian : ")
                src.cari_data_menu(varian, data_produk)
                print()
            elif menu == 3:
                varian_baru = produk_baru.Produk()
                new_id = gen.gen_id('produk')
                varian_baru.insert(new_id)
                data_produk.append(varian_baru.to_dict())
                handler.save_json("data_center/produk.json", data_produk)
                print("[System Status: Varian baru berhasil disimpan!]\n")
            elif menu == 4:
                while True:
                    nama_produk = input("Masukkan Nama Produk [0 untuk keluar]: ")
                    if nama_produk == '0': break
                    if validate.validasi_menu(nama_produk) == False:
                        print("Nama tidak valid\n")
                        continue
                    break
                if nama_produk == '0': break   
                while True:
                    try:
                        stok_tambah = int(input("Masukkan tambahan stok [0 untuk keluar]: "))

                        if stok_tambah == 0: break

                        indeks_menu = src.cari_indeks_menu(data_produk, nama_produk)
                        if validate.validasi_jumlah_stok(data_produk, saldo, indeks_menu, stok_tambah) == False:
                            print("Saldo tidak cukup")
                            continue
                        saldo -= data_produk[indeks_menu]['modal']*stok_tambah
                        data_produk[indeks_menu]['stok'] += stok_tambah
                        handler.save_json("data_center/produk.json", data_produk)
                        break
                    except ValueError: print("Hanya angka integer yang diperbolehkan")
                if stok_tambah == 0: break

            elif menu == 5:
                break
            else: print("\nMenu tidak ada\n")
        except ValueError: print("\nMenu hanya berupa angka bulat\n")

#memasukkan class Queue kedalam variabel antrian, dibuat diluar fungsi
#agar saat fungsi dipanggil lagi queue nya tidak hilang
antrian = queue.Queue()
def menu_3():
    global saldo
    global hari_ini

    data_produk = handler.load_json("data_center/produk.json")
    daftar_cabang = handler.load_json("data_center/cabang.json")
    data_member = handler.load_json("data_center/pelanggan.json")
    while True:
        tampilan_menu_3()
        data_pesanan_pelanggan = {}
        try:
            menu = int(input("Pilih Opsi (1-4): "))
            if menu == 1:
                while True:
                    gerobak = input("\nMasukkan nama Gerobak [0 untuk batal]: ")
                    if gerobak == '0':
                        break
                    if validate.validasi_gerobak(gerobak) == False:
                        print("Gerobak tak ditemukan, lihat keyword kembali")
                        continue

                    if validate.validasi_status_gerobak(daftar_cabang, gerobak) == False:
                        print("Status Gerobak Sedang Tutup, silahkan ubah status gerobak terlebih dahulu")
                        continue

                    data_gerobak = validate.validasi_gerobak(gerobak)
                    data_pesanan_pelanggan['nama gerobak'] = data_gerobak[0]
                    data_pesanan_pelanggan['kode gerobak'] = data_gerobak[1]
                    break

                if gerobak == '0':#jika user membatalkan pembuatan pesanan
                    break

                while True:
                    pesanan = []
                    nama_pelanggan = input("Masukkan Nama Pembeli: ").strip()
                    data_pesanan_pelanggan['nomor telepon'] = None
                    if validate.validasi_nama(nama_pelanggan) == False:
                        print("Nama tidak valid!")
                    while True:
                        membership_status = False
                        pilih_membership = input("Apakah anda memiliki member? [Y/N]").upper()
                        if pilih_membership == 'Y':
                            nomor = input("Masukkan Nomor Telepon Terdaftar: ")
                            membership_status = validate.validasi_status_membership(data_member,nomor)
                            if membership_status == False:
                                print("Nomor Tak Terdaftar")
                                continue
                            nama_pelanggan = membership_status
                            data_pesanan_pelanggan['nomor telepon'] = nomor
                            break
                        elif pilih_membership == 'N':
                            break
                        else: 
                            print("input tak valid")

                    data_pesanan_pelanggan['nama'] = nama_pelanggan
                    break

                while True:
                    pesanan_menu = input("Masukkan Menu [nama pastikan sesuai dengan daftar]: ")
                    if pesanan_menu == 'Susu Gepuk' or pesanan_menu == 'Susu' or pesanan_menu == 'Gepuk':
                        print("Masukkan nama menu langsung\n")
                        continue
                    if validate.validasi_menu(pesanan_menu) == False:
                        print("Menu Tidak Valid")
                        continue
                    else:
                        print("Menu ditemukan")

                    id_menu = src.input_menu(data_produk, pesanan_menu)
                    
                    pilih = -1 #menghindari error di kondisi if setelah ini
                    while True:
                        try:
                            jumlah_pesanan = int(input("Jumlah pesanan: "))
                            if validate.cek_stok(data_produk, id_menu, jumlah_pesanan)== False:
                                print("Stok tak cukup")
                                while True:
                                    pilih = input("Ganti pemesanan?(Y/N) ").upper()
                                    if pilih == "Y":
                                        print()
                                        break
                                    elif pilih == "N":
                                        break
                                    else: print("Masukkan input yang diminta!")

                                #validasi pilihan didalam while loop sebelumnya
                                if pilih == "Y":#kembali ke pesan menu varian
                                    print()
                                    break
                                elif pilih == "N":#kembali meminta pesanan
                                    continue

                            else: 
                                chamber = [id_menu, jumlah_pesanan]
                                pesanan.append(chamber)
                                break
                        except ValueError: print("Masukan hanya angka bulat")
                    
                    if pilih == 'Y':
                        continue

                    while True:
                        pesan_lagi = input("Pesan lagi (Y/N)? ").upper()
                        if pesan_lagi == 'Y':
                            print()
                            break
                        elif pesan_lagi == 'N':
                            total_harga = 0
                            data_pesanan_pelanggan['membership'] = False
                            data_pesanan_pelanggan['pesanan'] = pesanan

                            for i in range(len(pesanan)):
                                dummy, harga = src.cari_detail_menu(data_produk, pesanan[i][0])
                                total_harga += harga*pesanan[i][1]
                            
                            if membership_status != False:
                                membership_flag = True
                                data_pesanan_pelanggan['membership'] = membership_flag
                                idx = src.cari_indeks_member(data_member, nomor)
                                level_member = data_member[idx]['tingkat']

                                if hari_ini == 'Friday' and level_member == 'Premium':

                                    total_harga = total_harga*(10/100)                                                                  

                            data_pesanan_pelanggan['total harga'] = total_harga                           
                            print()
                            break
                        else: print("masukkan salah")
                    
                    if pesan_lagi == 'N':
                        break

                if pesan_lagi == "N":

                    if data_pesanan_pelanggan['total harga'] == 0:
                        break

                    id_antrean = gen.gen_id('antrian')
                    data_pesanan_pelanggan['id antrian'] = id_antrean
                    antrian.enqueue(data_pesanan_pelanggan) 
                    gen.gen_tampilan_pesanan(data_produk, data_pesanan_pelanggan, id_antrean)
                    print("[System Status: Pesanan berhasil dimasukkan]")   

                    
            elif menu == 2:
                data_transaksi = handler.load_json("data_center/transaksi.json")

                to_transaction = antrian.dequeue()
                if to_transaction['membership'] == True:
                    gen.save_poin(data_member, to_transaction['nomor telepon'], to_transaction['total harga'])
                    chamber = gen.sinkronisasi_poin(data_member, to_transaction['nomor telepon'])
                    data_member = chamber.copy()
                    handler.save_json("data_center/pelanggan.json", data_member)

                for i in range(len(daftar_cabang)):
                    if to_transaction['nama gerobak'] == daftar_cabang[i]['nama']:
                        for item in to_transaction['pesanan']:
                            daftar_cabang[i]['penjualan'] += item[1]
                            handler.kurangi_stok(data_produk, item[0], item[1]) 


                id_trx = gen.gen_id('transaksi')
                to_transaction['id transaksi'] = id_trx

                saldo+=to_transaction['total harga']
                data_transaksi.append(to_transaction)

                handler.save_json("data_center/cabang.json", daftar_cabang)
                handler.save_json("data_center/transaksi.json", data_transaksi)
                print("[System Status: Transaksi Berhasil!]\n")
                
            elif menu == 3:
                antrian.display(data_produk)

            elif menu == 4:
                break

            else: print("Menu tidak ada")

        except ValueError: print("\nMenu hanya berupa angka bulat")

def menu_4():
    #mengambil data riwayat transaksi langsung dari data center
    data_produk = handler.load_json("data_center/produk.json")
    data_transaksi = handler.load_json("data_center/transaksi.json")

    transaksi_dll = double_linked_list.DoublyLinkedList()
    for trx in data_transaksi:
        transaksi_dll.append(trx)

    #menampilkan header menu 4
    tampilan_menu_4()
    while True:
        print("[A] Tampilkan 3 Transaksi Terakhir")
        print("[B] Tampilkan Riwayat Transaksi")
        print("[C] Tampilkan Riwayat Transaksi dari Pembayaran Terbesar")
        print("[D] Keluar")
        choice = input("Pilih Opsi: ").upper()
        if choice == 'A':
            #jika file masih kosong
            if not data_transaksi:
                print("Menampilkan 3 data transaksi terbaru yang berhasil diproses.\n")
                print("="*55)
                print("Belum ada transaksi yang berhasil diproses.")
                print("="*55)
            else:
                print("Menampilkan 3 data transaksi terbaru yang berhasil diproses.\n")
                print("="*55)

                #memindahkan seluruh list transaksi ke stack
                stack_transaksi = stack.Stack()
                for trx in data_transaksi:

                    #inisialisasi untuk menampung riwayat ransaksi
                    stack_transaksi.push(trx)

                #mengambil data 3 transaksi paling terbaru
                tiga_trx_terbaru = stack_transaksi.menampilkan_transaksi(limit=3)

                #untuk menghitung dan mencetak 3 data transaksi yang sudah diambil
                for idx, trx_terbaru in enumerate (tiga_trx_terbaru):
                    if idx == 0:
                        print ("[TOP STACK]")

                #menghitung total bayar
                    total_bayar = 0
                    list_pesanan = trx_terbaru.get("pesanan", [])

                    for item in list_pesanan:
                        id_menu = item[0]
                        jumlah_beli = item[1]

                        #mencari harga dari data produk yang cocok
                        for produk in data_produk:
                            if produk.get('kode') == id_menu:
                                total_bayar += produk.get("harga", 0) * jumlah_beli
                                break

                    #mencetak nota riwayat transaksi
                    print(f"ID TRANSAKSI: {trx_terbaru.get("id transaksi")} ")
                    print(f"PELANGGAN   : {trx_terbaru.get("nama")} ")
                    print(f"LOKASI      :  {trx_terbaru.get("nama gerobak")} ({trx_terbaru.get("kode gerobak")})")
                    print(f"TOTAL BAYAR : Rp {total_bayar:,} ")
                    print(f"STATUS      : SELESAI ")
                    print("=" *55)

            print()
            input("tekan ENTER untuk kembali ke menu sebelumnya")
        
        elif choice == 'B':
            transaksi_dll.lihat_transaksi(data_produk)
        elif choice == 'C':
            data_trx = data_transaksi.copy()
            transaksi_urut = srt.selection_sort_transaksi(data_trx)
            for i in range(len(transaksi_urut)):
                pesanan = set()
                for item in transaksi_urut[i]['pesanan']:
                    bucket1, bucket_dummy = src.cari_detail_menu(data_produk, item[0])
                    pesanan.add(bucket1)
                print("-" * 50)
                print(f"ID Transaksi      : {transaksi_urut[i]['id transaksi']}")
                print(f"Nama Gerobak      : {transaksi_urut[i]['nama gerobak']} [{transaksi_urut[i]['kode gerobak']}]")
                print(f"Pelanggan         : {transaksi_urut[i]['nama']}")
                print(f"Jenis menu pesanan: {pesanan}")
                print(f"Total             : Rp {transaksi_urut[i]['total harga']},00")
            print()
        elif choice == 'D':
            break

        else: print("Opsi tak valid\n")



def menu_5():#fungsi untuk proses menu 5
    data_member = handler.load_json("data_center/pelanggan.json")
    data_member = gen.sinkronisasi_poin_all(data_member)

    member_ll = linked_list.LinkedList()
    for item in data_member:
        member_ll.append(item)
    
    hash_pelanggan = hash.HashTable(20)
    for pelanggan in data_member:
        hash_pelanggan.insert(pelanggan["telepon"],pelanggan)

    member_cll = circular_linked_list.CircularLinkedList()
    for pelanggan in data_member:
        member_cll.append(pelanggan)

    while True:
        try:
            tampilan_menu_5()
            menu = int(input("Pilih Opsi (1-4): "))

            if menu == 1:
                print("--- DAFTAR MEMBER SUSU GEPUK PEKANBARU ---")
                print("-"*60)
                member_ll.display()

            elif menu == 2:
                print("= CARI DATA MEMBER =")
                nomor = input("Masukkan Nomor Telepon: ")
                hasil = hash_pelanggan.search(nomor)
                if hasil is not None:
                    hasil_telepon = gen.format_telepon(hasil['telepon'])
                    print("[DATA DITEMUKAN]")
                    print("-"*30)
                    print(f"ID         : {hasil['id']}")
                    print(f"Nama       : {hasil['nama']}")
                    print(f"No. Telepon: {hasil_telepon}")
                    print(f"Poin       : {hasil['poin']}")
                    print(f"Level      : {hasil['tingkat']}\n")
                    print("-"*30)
                    if hasil['tingkat'] == 'Premium':
                        print("*catatan: Member Premium berhak mendapatkan diskon 10% setiap hari Jum'at")
                    print()
                    
                else:
                    print("Pelanggan tidak ditemukan\n")

                input("tekan ENTER untuk kembali ke menu 5")
                


            elif menu == 3:
                new_member = member.Member()
                print("== REGISTRASI MEMBER BARU ==")
                new_member.append()
                data_member_baru = new_member.to_dict()
                data_member.append(data_member_baru)

                member_ll.append(data_member_baru)

                hash_pelanggan.insert(data_member_baru["telepon"],data_member_baru)

                member_cll.append(data_member_baru)

                handler.save_json("data_center/pelanggan.json", data_member)
                print("Member Baru berhasil ditambahkan!\n")
            
            elif menu == 4:
                member_cll.lihat_member()
                
            elif menu == 5:
                break
            else: print("\nOpsi tidak ada\n")
        except ValueError: print("\ninput hanya berupa angka bulat\n")

def menu_6():
    data_cabang = handler.load_json("data_center/cabang.json")
    print("="*65)
    print("          D A T A  K E U A N G A N")
    print("="*65)
    keuntungan = gen.hitung_keuntungan(data_cabang)
    total_jual = gen.total_jual(data_cabang)
    print(f"Total saldo tersisa :  Rp. {saldo}")
    print(f"Total Keuntungan    :  Rp. {keuntungan}")
    print(f"Total Produk terjual:  {total_jual} produk")
    print("-"*65)
    print()
    input("Tekan ENTER untuk kembali ke menu utama...")

def system():#fungsi sistem utama
    global saldo
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
                menu_4()
            elif menu == 5:
                print()
                menu_5()
            elif menu == 6:
                menu_6()
            elif menu == 7:
                print()
                data_keuangan['saldo'] = saldo
                handler.save_json("data_center/keuangan.json", data_keuangan)
                print("Selesai")
                break
            else: print("Menu Tidak ada\n")
        except ValueError: print("Masukkan menu yang sesuai\n")              
            
system()