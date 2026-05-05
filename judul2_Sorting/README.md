# judul : Pengurutan Berat Barang Dengan Algoritma Bubble Sort

# Deskripsi singkat 

Program ini dibuat untuk mensimulasikan cara kerja dari algoritma bubble sort.program ini di buat untuk mengurutkan barang berdasarkan berat kemudian meminta user untuk menginput jumlah barangnya, nama barangnya beserta beratnya, lalu mengurutkannya dari berat terkecil ke terbesar (Ascending) menggunakan algoritma Bubble Sort.

algoritma yang digunakan adalah algoritma bubble sort yang mengurutkan nilai dengan membandingkannya dengan nilai sebelahnya kemudian menukar nilainya jika urutanya salah dilskukan terus menerus sampai semua nilainya terurut.

# source code
<img width="1234" height="1926" alt="code barang" src="https://github.com/user-attachments/assets/92f09717-0cdc-4ee5-a2cb-f423ca1efbd5" />

# penjelasan kode tiap barisnya

def tukar(arr, i, j): # fungsi untuk menukar dua elemen dalam array

temp = arr[i] # simpan sementara nilai arr[i] di variabel temp 

arr[i] = arr[j]  # isi arr[i] dengan nilai arr[j]

arr[j] = temp # isi arr[j] dengan nilai lama arr[i] (dari temp) yang membuat posisinya tertukar

def bubble_sort(arr, n): # fungsi Bubble Sort untuk mengurutkan data

for i in range(n - 1): # loop i dilakukan sebanyak (n-1) putaran

for j in range(n - i - 1): # loop j bandingkan elemen berdampingan

if arr[j][1] > arr[j + 1][1]: # bandingkan nilai elemen ke-j dengan elemen ke-(j+1)

tukar(arr, j, j + 1) # jika nilai kiri > nilai kanan, menjalankan fungsi tukar

def main(): # fungsi utama program

try:

n = int(input("Masukkan jumlah barang: "))  # minta jumlah barang dari user

except ValueError: # untuk mencegah user selain angka

print("Input tidak valid!") # jika bukan angka, tampilkan error

return # Hentikan fungsi main()

arr = [] # membuat array kosong untuk menampung data barang

print("Masukkan nama dan berat barang (kg):") # perintah input data

for i in range(n): # loop sebanyak n kali untuk input tiap barang

nama = input(f"Nama barang ke-{i+1}: ") # minta input nama barang ke-i

while True: # loop validasi input berat (ulangi jika input salah)

try:

berat = float(input(f"Berat {nama} (kg): "))  # minta input berat, konversi ke float

arr.append((nama, berat)) # menyimpan data sebagai tuple (nama, berat) ke array

break # jika input valid, keluar dari loop 

except ValueError: # untuk mencegah error jika input bukan angka

print("Input harus angka!") # error jika input bukan angka, minta input ulang

print("\nData sebelum diurutkan:") # Header tampilan data awal

for item in arr: # iterasi setiap tuple dalam array

print(item[0], "-", item[1], "kg") # cetak nama (index 0) dan berat (index 1) tiap barang

bubble_sort(arr, n) # panggil fungsi bubble sort untuk mengurutkan array

print("\nData setelah diurutkan:") # header tampilan data setelah diurutkan

for item in arr: # iterasi array yang sudah terurut

print(item[0], "-", item[1], "kg")  # cetak nama dan berat tiap barang yang sudah terurut

if __name__ == "__main__": # cek apakah file dijalankan langsung (bukan diimport)

main() # panggil fungsi main()

# output program

<img width="342" height="398" alt="Screenshot 2026-05-05 162654" src="https://github.com/user-attachments/assets/b70ea646-922d-433e-89c8-581b6fa53402" />

link video : 
