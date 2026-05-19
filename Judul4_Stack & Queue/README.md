# judul : program riwayat browser

## deskripsi singkat
program ini adalah simulasi dari riwayat pada browser yang meniru cara kerja tombol back dan forward pada browser untuk melihat riwayat website yang dikunjungi. dengan mwnggunakan struktur data stack lingked list dengan prinsip last in firs out(LIFO) yaitu data yang paling terakhir masuk akan menjdi yang pertama keluar menggunkan linked list untuk menghubungkan data dengan pointer.

## source code
<img width="1216" height="4282" alt="code stack browser" src="https://github.com/user-attachments/assets/f90e6ce1-1998-4878-a09f-55291d591af3" />

## penjelasan code 
1  Membuat kelas baru untuk node dalam linked list.

2  Membuat constructor yang akan otomatis terpanggil.

3  Menyimpan data ke dalam node.

4  Pointer ke node berikutnya, awalnya tidak terhubung.

7  Memebuat class stack untuk struktur data stack.

8  Constructor stack.

9  Menyimpan pointer ke elemen paling atas stack, awalnya kosong.

11  Fungsi cek apakah stack kosong.

12  Mengembalikan true jika stack kosong.

14  Fungsi menambah data ke paling atas stack.

15  Membuat node baru berisi data x.

16  Node baru diarahkan ke top lama.

17  Node baru dijadikan top stack.

19  Fungsi untuk menghapus data teratas stack.

20  Mengecek apakah stack kosong.

21  Kembalikan none jika kosong.

22  Simpan data dari node top sementara.

23  Pindah top_ptr ke node di bawahnya.

24  Mengembalikan data yang tadi disimpan.

26  Fungsi melihat data paling atas tanpa menghapusnya

27  Mengecek apakah stack kosong.

28  Jika kosong, mengembalikan none.

29  Mengembalikan data paling atas stack.

31  Fungsi untuk menampilkan semua isi stack.

32  Membuat list kosong untuk menyimpan hasil.

33  Variabel current untuk mulai dari node paling atas.

34  Telusuri sampai node paling bawah.

35  Menambahkan data node ke list hasil.

36  Geser ke node berikutnya.

37  Mengembalikan seluruh isi stack dalam bentuk list.

40  Class untuk mensimulasikan browser.

41  Constructor browser defaultnya adalah google.

42  Menyimpan halaman yang sedang dibuka.

43  Stack untuk menyimpan riwayat tombol Back.

44  Stack untuk menyimpan riwayat tombol Forward.

45  Menampilkan halaman awal browser.

47  Fungsi untuk membuka website baru.

48  Halaman sekarang dimasukkan ke back stack.

49  Forward stack dikosongkan.

50  Mengubah halaman sekarang menjadi URL baru.

51  Info halaman yang dikunjungi.

53  Fungsi tombol Back browser.

54  Mengecek apakah ada riwayat sebelumnya.

55  Menampilkan pesan jika halaman back kosong.

56  Menghentikan fungsi.

57  Halaman sekarang dipindahkan ke forward stack.

58  Mengambil halaman terakhir dari back stack.

59  Menampilkan halaman hasil back.

61  Fungsi tombol Forward browser.

62  Mengecek apakah ada riwayat forward.

63  Menampilkan pesan jika forward kosong.

64  Menghentikan fungsi.

65  Halaman sekarang masuk ke back stack.

66  Mengambil halaman dari forward stack.

67  Menampilkan halaman hasil forward.

70  Fungsi utama program.

71  Membuat objek browser.

72  Variabel menu pilihan.

74  Loop utama, berjalan sampai user memilih 4 (keluar)

76  Menampilkan menu kunjungi URL.

77  Menampilkan menu back.

78  Menampilkan menu forward.

79  Menampilkan menu keluar.

81  Menangani error input.

82  Input pilihan menu.

83  Menangkap error jika input bukan angka.

84  Menampilkan pesan error.

85  Mengulang loop.

87  Menu 1.

88  Input URL website, menghapus spasi kosong di awal/akhir.

89  Mengecek apakah URL tidak kosong.

90  Membuka website.

91-92 Menampilkan pesan jika URL kosong.

93-94 Menjalankan tombol back.

95-96 Menjalankan tombol forward.

97-98 Menutup program.

99-100 Menampilkan pesan jika menu tidak tersedia.

103 Mengecek apakah file dijalankan langsung.

104 Menjalankan fungsi utama program.

## output code

ketika memasukan URL web : 

<img width="289" height="177" alt="Screenshot 2026-05-19 214704" src="https://github.com/user-attachments/assets/b54aca08-c4db-443e-9431-6ef2a2412059" />

ketika menekan tombol back : 

<img width="239" height="134" alt="Screenshot 2026-05-19 214721" src="https://github.com/user-attachments/assets/ed59d6aa-0f2d-41d4-ba4e-b769624ae3ff" />

ketika menekan tombol forward  : 

<img width="211" height="130" alt="Screenshot 2026-05-19 214732" src="https://github.com/user-attachments/assets/cd4b3f5d-8531-45e3-a2d7-df469166c09f" />

link youtube : https://youtu.be/T-gw9X6J5Zg 
