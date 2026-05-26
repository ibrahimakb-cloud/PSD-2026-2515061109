# judul : sistem manajemen rating anime

## deskripsi singkat
Program ini adalah sistem manajemen rating anime yang menggunakan Binary Search Tree (BST) dengan rating sebagai key utama. Program memungkinkan user menambah anime, mencari berdasarkan rating, menampilkan daftar terurut, serta menemukan anime dengan rating tertinggi/terendah dan menghitung tinggi tree.

## source code
<img width="1940" height="5726" alt="code anime BST" src="https://github.com/user-attachments/assets/acaf5c0b-b5c9-45d2-ad84-59ff31270055" />


## penjelasan code 

1 Membuat kelas untuk node BST.

2 Constructor untuk Node dengan parameter self, judul, rating, penonton.

3 Menyimpan judul anime.

4 Menyimpan rating anime.

5 Menyimpan jumlah penonton.

6 Pointer ke anak kiri.

7 Pointer ke anak kanan.

10 Kelas BST. 

11 Constructor kelas BST dengan parameter self.

12 Membuat root yang awalnya kosong.

14 Fungsi rekursif atau memanggil dirinya sendiri untuk memasukkan node.

15 Saat posisi kosong.

16 Akan membuat node baru.

17 Jika rating yang dimasukan lebih kecil.

18 Masuk ke subtree kiri.

19 Jika rating yang dimasukan lebih besar.

20 Masuk ke subtree kanan.

21 Jika rating sama.

22 Mengganti data judul dengan yang baru.

23 Mengganti data penonton dengan yang baru.

24 Menampilkan pesan jika data telah diperbarui.

25 Kembalikan node saat ini.

27 Fungsi insert, yang dipanggil user. 

28 Memulai insert dari root.

30 Fungsi rekursif mencari anime berdasarkan rating.

31 Ketika node kosong atau ketika rating ditemukan.

32 Mengembalikan node.

33 Jika rating target lebih kecil.

34 Cari di subtree kiri.

35 Selain itu cari ke subtree kanan.

37 Fungsi search, yang dipanggil user.

38 Memulai pencarian dari root.

40 Fungsi mencari rating terkecil.

41 Jika tree kosong.

42 Maka kembalikan none atau kosong.

43 Membuat variabel curent untuk traversal.

44 Selama masih ada anak kiri.

45 Akan terus bergerak ke kiri.

46 Mengembalikan node paling kiri atau rating terkecil.

48 Fungsi mencari rating terbesar.

49 Jika tree kosong.

50 Maka kembalikan none atau kosong.

51 Membuat variabel curent untuk traversal.

52 Selama masih ada anak kanan.

53 Akan terus bergerak ke kanan.

54 Mengembalikan node paling kanan atau rating terbesar.

56 Fungsi Menampilkan anime secara terurut dari terkecil ke terbesar.

57 Jika node ada.

58 Pergi ke semua subtree kiri.

59 Menampilkan data judul, rating, dan penonton dari anime.

60 Kemudian kunjungi root kanan.

62 Fungsi hitung tinggi tree.

63 Jika root kosong.

64 Maka tinggi tree -1.

65 Jika tidak.

66 Hitung tinggi subtree kiri.

67 Hitung tinggi subtree kanan.

68 Kembalikan nilai sbutree tertinggi +1.

71 Fungsi utama program.

72 Membuat objek BST kosong.

74 Menambahkan data anime awal. 

75 Menambahkan data anime awal.

76 Menambahkan data anime awal.

78 Inisialisasi agar bisa masuk loop.

79 Loop utama, berjalan sampai user pilih 7.

80 Menampilkan pesan header.

81 Menampilkan opsi pilihan 1 tambah anime baru.

82 Menampilkan opsi pilihan 2 cari anime dari rating.

83 Menampilkan opsi pilihan 3 urutan anime dari rating terkecil ke terbesar.

84 Menampilkan opsi pilihan 4 anime dengan rating tertinggi.

85 Menampilkan opsi pilihan 5 anime dengan rating terendah.

86 Menampilkan opsi pilihan 6 tinggi dari tree.

87 Menampilkan opsi pilihan 7 keluar program.

88-89 Input pilihan user.

90 Jika bukan angka.

91 Tampilkan pesan error.

92 Kembali lagi ke awal loop.

93 Pilih 1 untuk input anime.

94 Input judul anime.

95-96 Input rating anime, diubah ke float.

97 Input jumlah penonton.

98 Menambahkan anime ke BST.

99 Menampilkan pesan anime telah ditambahkan.

100 Jika input bukan angka.

101 Tampilkan pesan error.

102 Kembali lagi ke awal loop.

103 Pilih 2 cari anime dari rating.

104-105 Input rating dari anime yang ingin dicari.

106 Melakukan pencarian dengan memanggil fungsi search.

107 Jika ditemukan.

108 Tampilkan pesan data ditemukan.

109 Tampilkan pesan judul anime.

110 Tampilkan pesan rating.

111 Tampilkan pesan jumlah penonton.

112 Jika tidak ditemukan.

113 Tampilkan pesan anime tidak ada.

114 Jika input bukan angka.

115 Tampilkan pesan input tidak valid.

116 Pilih 3 tampilkan semua anime secara terurut.

117 Tampilkan pesan daftar anime.

118 Mengecek apakah bst kosong.

119 Tampilkan pesan sistem masih kosong.

120 Jika tidak.

121 Panggil fungsi tampilkan_inoreder untuk mengurutkan anime.

122 Pilih 4 cari anime dengan rating tertinggi.

123 Memanggil fungsi max untuk mencari anime dengan rating tertinggi.

124 Jika max_rating ada.

125 Tampilkan pesan judul anime dan ratingnya.

126 Jika tidak.

127 Tampilkan pesan sistem masih kosong.

128 Pilih 5 cari anime dengan rating terendah.

129 Memanggil fungsi min untuk mencari anime dengan rating terendah.

130 Jika ada.

131 Tampilkan pesan judul anime dan ratingnya.

132 Jika tidak .

133 Tampilkan pesan sistem masih kosong.

134 Pilih 6 cari tinggi tree.

135 Hitung tinggi dari root.

136 Tampilkan pesan tinggi tree.

137 Pilih 7 keluar sistem.

138 Tampilkan pesan program selesai.

139 Jika input bukan angka pilihan. 

140 Tampilkan pesan input menu tidak valid.

142 Mengecek apakah program dijalankan lagsung.

143 Menjalankan fungsi utama program.

## output code

Pilihan 1 :

<img width="601" height="289" alt="Screenshot 2026-05-26 193318" src="https://github.com/user-attachments/assets/6a1530fc-fc09-4e39-85bd-89777756d0ab" />

Pilihan 2 :

<img width="610" height="347" alt="Screenshot 2026-05-26 193357" src="https://github.com/user-attachments/assets/454d6a08-9ac7-4afc-9179-f41b34d0196f" />

Pilihan 3 :

<img width="608" height="338" alt="Screenshot 2026-05-26 193414" src="https://github.com/user-attachments/assets/3dd00853-011e-4cda-b94b-d4b8dce13969" />

Pilihan 4 :

<img width="607" height="232" alt="Screenshot 2026-05-26 193433" src="https://github.com/user-attachments/assets/6af07814-a2a3-437b-be03-eb0daf5bb653" />

Pilihan 5 :

<img width="624" height="228" alt="Screenshot 2026-05-26 193444" src="https://github.com/user-attachments/assets/6ae6e931-4376-498d-ab19-ac18148adee5" />

Pilihan 6 :

<img width="596" height="224" alt="Screenshot 2026-05-26 193502" src="https://github.com/user-attachments/assets/edb3df7b-17e4-411a-b4c7-c94b419ae967" />

Pilihan 7:

<img width="617" height="221" alt="Screenshot 2026-05-26 193510" src="https://github.com/user-attachments/assets/1c562c73-c11c-438c-afcd-2226d9de88e3" />


link youtube : https://youtu.be/FnyqdZjDnHc 
