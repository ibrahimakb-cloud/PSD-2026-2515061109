nama_barang = {
    101: "Beras 5kg",
    102: "Minyak goreng 1L",
    103: "Gula 1kg",
    104: "Tepung terigu 1kg",
    105: "Susu 1L",
    106: "Telur 1 lusin",
}

def sequential_search(data, n, target):
    i = 0
    counter = 0
    while i < n:
        if data[i] == target:
            counter += 1
        i += 1
    return counter


def main():
    data = [
        101, 102, 101, 103, 104, 102, 101, 105,
        103, 102, 104, 101, 105, 103, 102, 104,
        101, 103, 105, 102
    ]

    n = len(data)
    while True:
        try:
            target = int(input("Masukkan kode produk yang ingin dicek: "))
            if target not in nama_barang:
                print("Kode produk tidak dikenali, silakan masukkan kode yang valid!\n")
                continue
            break
        except ValueError:
            print("Input tidak valid, silakan masukkan angka!\n")

    counter = sequential_search(data, n, target)

    if counter > 0:
        print(f"Nama Barang : {nama_barang[target]}")
        print(f"Kode Produk : {target}")
        print(f"Jumlah Stok : {counter} unit")
    else:
        print(f"Stok untuk kode produk {target} ({nama_barang[target]}) tidak tersedia.")

if __name__ == "__main__":
    main()
