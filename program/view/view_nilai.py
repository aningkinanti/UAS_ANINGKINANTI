#author aningkinanti

from model.daftar_nilai import kontak

def header():
    print("\n-----------------------------------------------------------------------------------------------")
    print("---------------------------------------PROGRAM INPUT DATA--------------------------------------")
    print("-----------------------------------------------------------------------------------------------")
    print("|    (T)Tambah     |    (U)Ubah    |      (H)Hapus     |      (C)Cari      |     (L)Lihat     |")
    print("-----------------------------------------------------------------------------------------------")


def notoption():
    print("----------------------------")
    print("--Pilih opsi yang tersedia--")
    print("----------------------------")
    print("    (T)Tambah       (U)Ubah      (H)Hapus     (C)Cari      (L)Lihat  ")


def cetak():
    print("\n-----------------------------------------------------------------------------------------------")
    print("--------------------------------------DAFTAR DATA MAHASISWA------------------------------------")
    print("-----------------------------------------------------------------------------------------------")
    print("| NO |      NAMA       |       NIM        | NILAI TUGAS | NILAI UTS | NILAI UAS | NILAI AKHIR |")
    print("|----|-----------------|------------------|-------------|-----------|-----------|-------------|")
    no = 1
    for tabel in kontak.values():
        print("|{0:3} | {1:15} | {2:16} | {3:11} | {4:9} | {5:9} | {6:11.2f} |"
              .format(no, tabel[0], tabel[1], tabel[2], tabel[3], tabel[4], tabel[5]))
        no += 1
    print("-----------------------------------------------------------------------------------------------")
    print("\n    (T)Tambah       (U)Ubah      (H)Hapus     (C)Cari      (L)Lihat   ")


def cari():
    from view.input_nilai import cari
    cari()
    print("    (T)Tambah       (U)Ubah      (H)Hapus     (C)Cari      (L)Lihat   ")