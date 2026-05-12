# Judul sistem pengecekan stock barang di gudang

## Deskripsi singkat
Program ini adalah sistem pengecekan stok barang gudang yang menggunakan algoritma Sequential Search untuk menghitung berapa unit suatu barang tersedia di gudang  berdasarkan kode produk yang diinputkan user.
Menggunakan algoritma pencarian sequential search untuk mencari keseluruh array menelusuri array satu per satu dari awal hingga akhir, menghitung setiap kemunculan kode target yang dicari.
## source code 
<img width="1680" height="2116" alt="code gudang" src="https://github.com/user-attachments/assets/c549266c-dd2b-4145-b4af-c7494627967a" />

## penjelasan kode
1-8 membuat dictionary bernama nama_barang yang bisa menyimpan pasangan data key dan value untuk menyimpan kode barang sebagai key dan nama barang sebagai value
contohnya : 101 (key) : Beras 5kg (value) 

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
<img width="547" height="153" alt="Screenshot 2026-05-12 005748" src="https://github.com/user-attachments/assets/dffe4385-a12d-4cc0-9da2-cf654a4ec61a" />
link youtube : 
