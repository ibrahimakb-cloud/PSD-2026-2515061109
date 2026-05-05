def tukar(arr, i, j):
    temp = arr[i]
    arr[i] = arr[j]
    arr[j] = temp

def bubble_sort(arr, n):
    for i in range(n - 1):
        for j in range(n - i - 1):
            if arr[j][1] > arr[j + 1][1]:
                tukar(arr, j, j + 1)

def main():
    try:
        n = int(input("Masukkan jumlah barang: "))
    except ValueError:
        print("Input tidak valid!")
        return

    arr = []
    print("Masukkan nama dan berat barang (kg):")
    for i in range(n):
        nama = input(f"Nama barang ke-{i+1}: ")
        
        while True:
            try:
                berat = float(input(f"Berat {nama} (kg): "))
                arr.append((nama, berat))  
                break
            except ValueError:
                print("Input harus angka!")

    print("\nData sebelum diurutkan:")
    for item in arr:
        print(item[0], "-", item[1], "kg")

    bubble_sort(arr, n)

    print("\nData setelah diurutkan:")
    for item in arr:
        print(item[0], "-", item[1], "kg")

if __name__ == "__main__":
    main()