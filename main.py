from utility import file_handler as handler
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
    print("1. Manajemen Gerobak")
    print("2. Menu Varian Susu Gepuk")
    print("3. Pemesanan/Kasir Antrean")
    print("4. Riwayat Transaksi Terakhir")
    print("5. Data Pelanggan Terdaftar")
    print("6. Simpan Data dan Keluar")
    print("="*55)

def tampilan_menu_1():
    print("-"*55)
    print("DAFTAR GEROBAK SUSU GEPUK")
    print("-"*55)

def tampilan_menu_2():
    print("="*55)
    print("            V A R I A N  S U S U  G E P U K")
    print("="*55)
    print()
    print("[1] Lihat Semua Menu")
    print("[2] Urutan Harga Termurah")
    print("[3] Cari Varian Rasa")
    print("[4] Kembali Ke Menu Utama")
    print()
    print("="*55)

def tampilan_menu_3():
    pass

def tampilan_menu_4():
    pass

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
    tampilan_menu_1()

def menu_2():
    while True:
        try:
            tampilan_menu_2()
            menu = int(input("Pilih Opsi (1-4): "))
            if menu == 1:
                pass
            elif menu == 2:
                pass
            elif menu == 3:
                pass
            elif menu == 4:
                break
        except ValueError: 
            print()
            print("Menu hanya berupa angka bulat")

def menu_3():
    pass

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
            else:
                print() 
                print("Opsi tidak ada")
        except ValueError: 
            print()
            print("input hanya berupa angka bulat")
            print()

def system():#fungsi sistem utama
    while True:
        try:
            tampilkan_menu_utama()
            menu = int(input("Pilih Menu (1-6): "))
            if menu == 1:
                print()
                menu_1()
                continue
            elif menu == 2:
                print()
                menu_2()
            elif menu == 3:
                print()
                continue
            elif menu == 4:
                print()
                continue
            elif menu == 5:
                print()
                menu_5()
                continue
            elif menu == 6:
                print()
                print("Selesai")
                break
            else:
                print() 
                print("Menu Tidak ada")
        except ValueError: 
            print()
            print("Masukkan menu yang sesuai")
            print()               
            

system()