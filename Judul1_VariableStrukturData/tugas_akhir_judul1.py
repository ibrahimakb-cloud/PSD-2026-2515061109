def menu():
    print("1. Cek Status Wadah Telur")
    print("2. Tambah Telur")
    print("3. Cek Alamat Memori")
    print("4. Keluar")

def main():
    kapasitas = 4
    jumlah_telur = 0

    wadah_telur = ["[Kosong]"] * kapasitas
    
    running = True

    while running:
        menu()
        try:
            choice = int(input("Pilih menu: "))
        except ValueError:
            print("Masukkan angka yang valid!")
            continue

        if choice == 1:
            print("\nIsi Wadah:")
            for i in range(kapasitas):
                print(f"Slot {i}: {wadah_telur[i]}")

        elif choice == 2:
            print("menambah telur")
            if jumlah_telur == kapasitas:
                print(" wadah sudah penuh")
                
                kapasitas_baru = kapasitas + 1
                print(f"membuat wadah baru dengan kapasitas {kapasitas_baru}")

                wadah_baru = ["[Kosong]"] * kapasitas_baru
                
                print("Memindahkan telur ke wadah baru")
                for i in range(kapasitas):
                    wadah_baru[i] = wadah_telur[i]
                
                wadah_telur = wadah_baru
                kapasitas = kapasitas_baru
                print("Wadah berhasil diperbesar")

            wadah_telur[jumlah_telur] = "Telur"
            print(f"\nBerhasil meletakkan telur di Slot {jumlah_telur}.")
            jumlah_telur += 1 

        elif choice == 3:
            print(f"\nAddress Wadah Telur: {id(wadah_telur)}")

        elif choice == 4:
            running = False
            print("\nSelesai.")

        else:
            print("Pilihan tidak valid.")

if __name__ == "__main__":
    main()