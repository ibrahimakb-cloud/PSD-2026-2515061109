class NodeAnime:
    def __init__(self, judul, rating, penonton):
        self.judul = judul
        self.rating = round(rating, 1)
        self.penonton = penonton
        self.left = None
        self.right = None


class SistemAnimeBST:
    def __init__(self):
        self.root = None

    def _insert(self, root, judul, rating, penonton):
        if root is None:
            return NodeAnime(judul, rating, penonton)
        if rating < root.rating:
            root.left = self._insert(root.left, judul, rating, penonton)
        elif rating > root.rating:
            root.right = self._insert(root.right, judul, rating, penonton)
        else:
            root.judul = judul
            root.penonton = penonton
            print(f"[Info] Rating {rating} sudah ada, data anime diperbarui!")
        return root

    def insert(self, judul, rating, penonton):
        self.root = self._insert(self.root, judul, rating, penonton)

    def _search(self, root, rating):
        if root is None or root.rating == rating:
            return root
        if rating < root.rating:
            return self._search(root.left, rating)
        return self._search(root.right, rating)

    def search(self, rating):
        return self._search(self.root, rating)

    def find_min(self, root):
        if root is None:
            return None
        current = root
        while current.left is not None:
            current = current.left
        return current

    def find_max(self, root):
        if root is None:
            return None
        current = root
        while current.right is not None:
            current = current.right
        return current

    def tampilkan_inorder(self, root):
        if root is not None:
            self.tampilkan_inorder(root.left)
            print(f"- {root.judul:<30} | Rating: {root.rating:<5} | Penonton: {root.penonton:,}")
            self.tampilkan_inorder(root.right)

    def height(self, root):
        if root is None:
            return -1
        else:
            left_height = self.height(root.left)
            right_height = self.height(root.right)
            return max(left_height, right_height) + 1


def main():
    bst = SistemAnimeBST()
    
    bst.insert("gurren lagann", 9.9, 279263947)
    bst.insert("petualangan aneh jojo", 8.6, 505890287)
    bst.insert("Mob Psycho 100", 9.7, 30400503)
    
    pilih = 0
    while pilih != 7:
        print("\n=== SISTEM RATING ANIME (BST) ===")
        print("1. Tambah Anime Baru")
        print("2. Cari Anime Berdasarkan Rating")
        print("3. Tampilkan Semua urutan Anime dari rating terkecil ke terbesar")
        print("4. anime dengan rating tertinggi")
        print("5. anime dengan rating terendah")
        print("6. tinggi tree")
        print("7. Keluar")
        try:
            pilih = int(input("Pilih: "))
        except ValueError:
            print("Input tidak valid!")
            continue
        if pilih == 1:
            judul = input("Masukkan Judul Anime : ")
            try:
                rating = float(input("Masukkan Rating (0-10): "))
                penonton = int(input("Masukkan Jumlah Penonton: "))
                bst.insert(judul, rating, penonton)
                print(f"'{judul}' berhasil ditambahkan ke dalam sistem!")
            except ValueError:
                print("Input rating atau penonton tidak valid!")
                continue
        elif pilih == 2:
            try:
                cari_rating = float(input("Masukkan rating anime yang dicari: "))
                hasil = bst.search(cari_rating)
                if hasil:
                    print(f"\n[Data Ditemukan]")
                    print(f"Judul    : {hasil.judul}")
                    print(f"Rating   : {hasil.rating}")
                    print(f"Penonton : {hasil.penonton:,}")
                else:
                    print(f"Anime dengan rating {cari_rating} tidak ditemukan.")
            except ValueError:
                print("Input rating tidak valid!")
        elif pilih == 3:
            print("\n--- Daftar anime dari rating terkecil ke terbesar ---")
            if bst.root is None:
                print("(Sistem masih kosong)")
            else:
                bst.tampilkan_inorder(bst.root)
        elif pilih == 4:
            max_rating = bst.find_max(bst.root)
            if max_rating is not None:
                print(f"Anime dengan rating tertinggi: {max_rating.judul} (Rating: {max_rating.rating})")
            else:
                print("(Sistem masih kosong)")
        elif pilih == 5:
            min_rating = bst.find_min(bst.root)
            if min_rating is not None:
                print(f"Anime dengan rating terendah: {min_rating.judul} (Rating: {min_rating.rating})")
            else:
                print("(Sistem masih kosong)")
        elif pilih == 6:
            h = bst.height(bst.root)
            print(f"Ketinggian tree: {h}")
        elif pilih == 7:
            print("Program selesai. Sampai jumpa!")
        else:
            print("Pilihan menu tidak valid!")

if __name__ == "__main__":
    main()