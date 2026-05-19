class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class Stack:
    def __init__(self):
        self.top_ptr = None

    def is_empty(self):
        return self.top_ptr is None

    def push(self, x):
        new_node = Node(x)
        new_node.next = self.top_ptr
        self.top_ptr = new_node

    def pop(self):
        if self.is_empty():
            return None
        data = self.top_ptr.data
        self.top_ptr = self.top_ptr.next
        return data

    def peek(self):
        if self.is_empty():
            return None
        return self.top_ptr.data

    def display_all(self):
        result = []
        current = self.top_ptr
        while current is not None:
            result.append(current.data)
            current = current.next
        return result


class RiwayatBrowser:
    def __init__(self, halaman_awal="google"):
        self.halaman_saat_ini = halaman_awal
        self.back_stack = Stack()
        self.fwd_stack  = Stack()
        print(f"Browser dibuka {self.halaman_saat_ini}")

    def kunjungi(self, url):
        self.back_stack.push(self.halaman_saat_ini)
        self.fwd_stack = Stack()
        self.halaman_saat_ini = url
        print(f"Mengunjungi : {url}")

    def back(self):
        if self.back_stack.is_empty():
            print("Tidak ada halaman sebelumnya.")
            return
        self.fwd_stack.push(self.halaman_saat_ini)
        self.halaman_saat_ini = self.back_stack.pop()
        print(f"Back : {self.halaman_saat_ini}")

    def forward(self):
        if self.fwd_stack.is_empty():
            print("Tidak ada halaman berikutnya.")
            return
        self.back_stack.push(self.halaman_saat_ini)
        self.halaman_saat_ini = self.fwd_stack.pop()
        print(f"Forward : {self.halaman_saat_ini}")


def main():
    browser = RiwayatBrowser()
    pilih = 0

    while pilih != 4:

        print("1. Kunjungi URL")
        print("2. Tombol Back (←)")
        print("3. Tombol Forward (→)")
        print("4. Keluar")

        try:
            pilih = int(input("Pilih: "))
        except ValueError:
            print("Input tidak valid!")
            continue

        if pilih == 1:
            url = input("Masukkan URL website : ").strip()
            if url:
                browser.kunjungi(url)
            else:
                print("URL tidak boleh kosong.")
        elif pilih == 2:
            browser.back()
        elif pilih == 3:
            browser.forward()
        elif pilih == 4:
            print("Browser ditutup.")
        else:
            print("Pilihan tidak valid!")


if __name__ == "__main__":
    main()
