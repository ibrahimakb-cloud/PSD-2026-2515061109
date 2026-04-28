# Judul : Program penyimpanan Telur ayam

# deskripsi singkat  
Program ini dibuat untuk mensimulasikan bagaimana  Dynamic Array (Vector) bekerja. Program menunjukkan bahwa sebuah array yang awalnya memiliki batas (kapasitas), bisa membuat wadah baru yang lebih besar dan memindahkan data lama ke dalamnya saat sudah penuh.
Algoritma dan struktur data yang di gunakan adalah dynamic array (vector) yang bisa membuat wadah baru dengan kapasitas lebih banyak saat wadah lama yang digunakan sudah penuh dan memindahkan data sebelumnya ke wadah baru.

Algoritma dan struktur data yang di gunakan adalah dynamic array (vector) yang bisa membuat wadah baru dengan kapasitas lebih banyak saat wadah lama yang digunakan sudah penuh dan memindahkan data sebelumnya ke wadah baru.

# Source Code
<img width="1510" height="2610" alt="code_telur" src="https://github.com/user-attachments/assets/0c4e4026-23a8-4144-91e9-64622068f32d" />

# penjelasan kode tiap barisnya :

def menu(): # fungsi untuk menampilkan menu

print("1. Cek Status Wadah Telur") # opsi 1 - melihat isi semua slot

print("2. Tambah Telur") # opsi 2 - menambahkan telur ke wadah

print("3. Cek Alamat Memori") # opsi 3 - melihat address memori array

print("4. Keluar") # opsi 4 - keluar program

def main(): # fungsi utama program

kapasitas = 4 # kapasitas awal wadah = 4 slot

jumlah_telur = 0 # counter untuk mengetahui telur yang sudah diisi, awalnya 0

wadah_telur = ["[Kosong]"] * kapasitas # buat array awal yang berisi [kosong] sebanyak kapasitas (4)

running = True # variabel pengontrol agar loop terus berjalan

while running: # loop berjalan selama 'running' True

menu() # memanggil fungsi menu

try:

choice = int(input("Pilih menu: ")) # minta input pilihan user, ubah ke integer

except ValueError:

print("Masukkan angka yang valid!") # error Jika bukan angka  
            
continue # kembali ke awal loop

if choice == 1: # jika user memilih opsi 1

print("\nIsi Wadah:") # mencetak header

for i in range(kapasitas): # melakukan Iterasi sebanyak jumlah kapasitas

print(f"Slot {i}: {wadah_telur[i]}") # mencetak isi tiap slot beserta indexnya

elif choice == 2: # jika user memilih opsi 2 

print("menambah telur") # mencetak info penambahan

if jumlah_telur == kapasitas: # mengecek apakah semua slot sudah terisi penuh?

print(" wadah sudah penuh") # mencetat info jika wadah penuh

kapasitas_baru = kapasitas + 1 # menambah kapasitas, kapasitas lama +1
                
print(f"membuat wadah baru dengan kapasitas {kapasitas_baru}") # mencetak info pembuatan wadah baru

wadah_baru = ["[Kosong]"] * kapasitas_baru  # membuat array baru yang lebih besar 

print("Memindahkan telur ke wadah baru") # mencetak info proses copy data
                
for i in range(kapasitas): # melakukan loop dari 0 sampai kapasitas lama
                    
wadah_baru[i] = wadah_telur[i] # memindahkan elemen (telur) ke wadah baru

wadah_telur = wadah_baru # ganti referensi wadah_telur menunjuk ke array baru
                
kapasitas = kapasitas_baru # update variabel kapasitas ke ukuran baru
                
print("Wadah berhasil diperbesar") # mencetak info resize berhasil

(Blok ini akan dijalankan setelah mengecek ada ruang (sebelum dan setelah resize))
            
wadah_telur[jumlah_telur] = "Telur" # isi slot pada index jumlah_telur dengan "Telur"
            
print(f"\nBerhasil meletakkan telur di Slot {jumlah_telur}.")  # mencetak info posisi telur
            
jumlah_telur += 1 # tambah counter telur sebanyak 1

elif choice == 3: # jika user memilih opsi 3
            
print(f"\nAddress Wadah Telur: {id(wadah_telur)}") # menampilkan alamat memori array saat ini

elif choice == 4: # jika user memilih opsi 4
            
running = False # buat variabel untuk menghentikan loop
            
print("\nSelesai.") # tampilkan pesan selesai
     
else: # jika input angka tapi bukan 1-4
           
print("Pilihan tidak valid.") # tampilkan pesan tidak valid

if __name__ == "__main__": # cek apakah file dijalankan langsung (bukan diimport modul lain)

main() # panggil fungsi main() untuk menjalankan program

# Output Code

<img width="1392" height="728" alt="Screenshot 2026-04-28 140101" src="https://github.com/user-attachments/assets/a858b021-4946-47e3-83b6-3c42b5800682" />
link video : 
https://youtu.be/3OuKqqBhtac
