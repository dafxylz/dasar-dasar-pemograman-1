buku = {
    "buku1": {
        "judul": "Bumi",
        "penulis": "Tere Liye",
        "tahun_terbit": 2014
    },
    "buku2": {
        "judul": "Bulan",
        "penulis": "Tere Liye",
        "tahun_terbit": 2019
    },
    "buku3": {
            "judul": "matahari",
            "penulis": "Tere Liye",
            "tahun_terbit": 2017
    }
}

while True:
    print("\nData Buku Anda")
    print("1. Tampilkan buku")
    print("2. Tambah Penerbit buku")
    print("3. Ubah Penulis buku")
    print("4. Hapus Penerbit buku")
    print("5. Keluar")

    pilih = input("Pilih menu: ")

    if pilih == "1":
        print("\nData Buku Anda:")
        print(buku["buku1"])
        print(buku["buku2"])
        print(buku["buku3"])

    elif pilih == "2":
        print("\ntambah penerbit buku")
        print("buku1")
        print("buku2")
        print("buku3")
        pilih_buku = input("Pilih buku: ")      
        if pilih_buku in buku:
            buku[pilih_buku]["penerbit"] = input("Penerbit: ")
            print("Penerbit berhasil ditambahkan.")
        else:
            print("Buku tidak ditemukan.")

    elif pilih == "3":
        print("\nubah penulis buku")
        print("buku1")
        print("buku2")
        print("buku3")
        pilih_buku = input("Pilih buku : ")
        if pilih_buku in buku:
            buku[pilih_buku]["penulis"] = input("Penulis baru: ")
            print("Penulis berhasil diubah.")
        else:
            print("Buku tidak ditemukan.")

    elif pilih == "4":
        print("buku1")
        print("buku2")
        print("buku3")
        pilih_buku = input("Pilih buku :")
        if pilih_buku in buku:
            buku[pilih_buku].pop("penerbit", None)
            print("Penerbit berhasil dihapus.")
        else:
            print("Buku tidak ditemukan.")

    elif pilih == "5":
        print("\nData akhir buku anda:")
        print(buku["buku1"])
        print(buku["buku2"])
        print(buku["buku3"])
        break

    else:
        print("Menu tidak tersedia.")

