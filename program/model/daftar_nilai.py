#author aningkinanti

kontak = {}


def tambah_kontak(nama,nim,nTugas,nUts,nUas):
    nAkhir = float(nTugas)*30/100+(nUts)*35/100+(nUas)*35/100
    kontak[nama] = nama,nim,nTugas,nUts,nUas,nAkhir


def ubah_kontak(nama):
    if nama in kontak.keys():
        del kontak[nama]
        print("\n---Masukan Perubahan Data---")
        from view.input_nilai import inputan
        inputan()
    else:
        print(" ________________________")
        print("| Data {} tidak ditemukan |".format(nama))
        print(" ‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾")
        print("    (T)Tambah       (U)ubah      (H)Hapus     (C)Cari      (L)Lihat   ")


def cari(nama):
    if nama in kontak.keys():
        print("\n-----------------------------------------------------------------------------------------")
        print("|      NAMA       |       NIM        | NILAI TUGAS | NILAI UTS | NILAI UAS | NILAI AKHIR |")
        print("|-----------------|------------------|-------------|-----------|-----------|-------------|")
        print("| {0:15} | {1:16} | {2:11} | {3:9} | {4:9} | {5:11.2f} |".format(nama, kontak[nama][1], kontak[nama][2],kontak[nama][3],kontak[nama][4], kontak[nama][5]))
        print("------------------------------------------------------------------------------------------")
    else:
        print(" ________________________")
        print("| Data {} tidak ditemukan |".format(nama))
        print(" ‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾")


def hapus(nama):
    if nama in kontak.keys():
        del kontak[nama]
        return True
    else:
        print(" ________________________")
        print("| Data {} tidak ditemukan |".format(nama))
        print(" ‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾")
        return False