# Judul sistem pengecekan stock barang di gudang

## Deskripsi singkat
Program ini adalah sistem pengecekan stok barang gudang yang menggunakan algoritma Sequential Search untuk menghitung berapa unit suatu barang tersedia di gudang  berdasarkan kode produk yang diinputkan user.
Menggunakan algoritma pencarian sequential search untuk mencari keseluruh array menelusuri array satu per satu dari awal hingga akhir, menghitung setiap kemunculan kode target yang dicari.
## source code 
<img width="1680" height="2116" alt="code gudang" src="https://github.com/user-attachments/assets/c549266c-dd2b-4145-b4af-c7494627967a" />

## penjelasan kode
1 membuat dictionary bernama nama_barang yang bisa menyimpan pasangan data key dan value untuk menyimpan kode barang sebagai key dan nama barang sebagai value

2 data barang 101 (key) : Beras 5kg (value) 

3 data barang 102 (key) : Minyak goreng 1L (value)

4 data barang 103 (key) : Gula 1kg (value)

5 data barang 104 (key) : tepung terigu 1kg (value)

6 data barang 105 (key) : Susu 1L (value)

7 data barang 106 (key) : Telur 1 lusin (value)

10 membuat fungsi sequential_serach dengan parameter data, n dan target

11 digunakan agar perhitungan index dimulai dari 0 (elemen pertama)

12 variabel counter untuk menghitung berapa kali target muncul dalam array

13 perulangan i yang akan terus berjalan selama i lebih kecil dari n atau jumlah data digunakan untuk mengeccek elemen dalam list satu-persatu

14 mengecek apakah elemen dalam index i sama dengan elemen target atau kode yang dicari

15 jika elemen cocok akan menambahkan couter sebanyak 1

16 tambah index i agar perulangan berpindah ke data selanjutnya

17 mengembalikan total kemunculan target dalam list data

20 fungsi utama dari program

21-25 membuat list data yang berisi kode-kode produk setiap elemen = 1 stock barang

27 menghitung seluruh data dan disimpan dalam variabel n

28 perulangan untuk input, loop akan terus berjalan jika user memasukan data yang salah

29 untuk menagani kemungkinan saat error

30 meminta user untuk memasukan kode produk 

31 mengecek jika target yang dicari tidak ada dalam nama_barang

32 menampilkan pesan kode produk tidak valid

33 kembali ke awal loop untuk meminta input ulang

34 jika input valid loop akan selesai

35-36 menangkap error jika input bukan angka kemudian menampilkan pesan error input bukan angka

38 memanggil fungsi sequetial_search dan menyimpan hasil pencarian stock

40-43 jika jumlah counter lebih dari 0 maka akan menampilkan pesan nama barang, kode produk, dan jumlah stock produk

44-45 jika counter 0 atau barang tidak ditemukan maka akan menampilkan pesan bahwa stock barang tersebut kosong

47 digunakan untuk mengecek apakah file dijalankan langsung

48 jika iya akan menjalankan fungsi main
## output code
output jika input angka tapi bukan kode di nama_barang :

<img width="558" height="38" alt="Screenshot 2026-05-12 212629" src="https://github.com/user-attachments/assets/dcc0f3eb-84bc-403b-8586-0e0929bd27f3" />

output jika input selain angka :

<img width="390" height="42" alt="Screenshot 2026-05-12 212640" src="https://github.com/user-attachments/assets/d617ba5c-80ec-45ae-b584-f5e6cd46c6b7" />

output jika input benar :

<img width="390" height="87" alt="Screenshot 2026-05-12 212659" src="https://github.com/user-attachments/assets/81b1b485-1130-4be8-b200-e08d649d9386" />

output jika barang tidak ada di dalam gudang :

<img width="528" height="42" alt="Screenshot 2026-05-12 212709" src="https://github.com/user-attachments/assets/2b7718e9-7855-4b73-aa4a-1f82f6fdc6b1" />

link youtube : https://youtu.be/NQyKDTgXej4

tugas : 
<img width="1172" height="1599" alt="WhatsApp Image 2026-05-12 at 21 59 48" src="https://github.com/user-attachments/assets/14d303cd-4ae6-4b35-99af-ef9fce8d0383" />
