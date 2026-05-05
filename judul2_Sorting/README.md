# judul : Pengurutan Berat Barang Dengan Algoritma Bubble Sort

# Deskripsi singkat 

Program ini dibuat untuk mensimulasikan cara kerja dari algoritma bubble sort.program ini di buat untuk mengurutkan barang berdasarkan berat kemudian meminta user untuk menginput jumlah barangnya, nama barangnya beserta beratnya, lalu mengurutkannya dari berat terkecil ke terbesar (Ascending) menggunakan algoritma Bubble Sort.

algoritma yang digunakan adalah algoritma bubble sort yang mengurutkan nilai dengan membandingkannya dengan nilai sebelahnya sampai semua nilainya terurut.

# source code
<img width="1234" height="1926" alt="code barang" src="https://github.com/user-attachments/assets/92f09717-0cdc-4ee5-a2cb-f423ca1efbd5" />

# penjelasan kode tiap barisnya

def tukar(arr, i, j):        # Fungsi untuk menukar dua elemen dalam array
temp = arr[i]            # Simpan sementara nilai arr[i] ke variabel temp agar tidak hilang
arr[i] = arr[j]          # Isi arr[i] dengan nilai arr[j]
arr[j] = temp            # Isi arr[j] dengan nilai lama arr[i] (dari temp)
                             # → Hasil: posisi elemen i dan j berhasil ditukar
def bubble_sort(arr, n):          # Fungsi Bubble Sort, menerima array dan jumlah elemen (n)
for i in range(n - 1):        # Loop luar: sebanyak (n-1) putaran/pass
                                  # Setiap putaran memastikan 1 elemen terbesar "menggelembung" ke akhir
for j in range(n - i - 1):        # Loop dalam: bandingkan elemen berdampingan
                                          # Batas berkurang tiap putaran karena elemen akhir sudah terurut
if arr[j][1] > arr[j + 1][1]: # Bandingkan BERAT (index [1]) elemen ke-j dengan elemen ke-(j+1)
tukar(arr, j, j + 1)      # Jika berat kiri > berat kanan, tukar posisinya
def main():                               # Fungsi utama program
try:
n = int(input("Masukkan jumlah barang: "))  # Minta jumlah barang dari user, konversi ke integer
except ValueError:
print("Input tidak valid!")       # Jika bukan angka, tampilkan error
return                            # Hentikan fungsi main(), program selesai
arr = []                              # Inisialisasi array kosong untuk menampung data barang
print("Masukkan nama dan berat barang (kg):")  # Instruksi input data
 for i in range(n):                    # Loop sebanyak n kali untuk input tiap barang
nama = input(f"Nama barang ke-{i+1}: ")   # Minta input nama barang ke-i
 while True:                       # Loop validasi input berat (ulangi jika input salah)
try:
berat = float(input(f"Berat {nama} (kg): "))  # Minta input berat, konversi ke float
arr.append((nama, berat))                      # Tambahkan tuple (nama, berat) ke array
break                                          # Input valid, keluar dari loop validasi
except ValueError:
print("Input harus angka!")   # Jika bukan angka/desimal, minta input ulang
 print("\nData sebelum diurutkan:")    # Header tampilan data awal
for item in arr:                      # Iterasi setiap tuple dalam array
print(item[0], "-", item[1], "kg")  # Cetak nama (index 0) dan berat (index 1) tiap barang
bubble_sort(arr, n)                   # Panggil fungsi bubble sort untuk mengurutkan array
print("\nData setelah diurutkan:")    # Header tampilan data setelah diurutkan
for item in arr:                      # Iterasi array yang sudah terurut
print(item[0], "-", item[1], "kg")  # Cetak nama dan berat tiap barang (urutan berat terkecil→terbesar)


if __name__ == "__main__":   # Cek apakah file dijalankan langsung (bukan diimport)
    main()                   # Panggil fungsi main()
