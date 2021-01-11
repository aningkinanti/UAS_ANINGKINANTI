#author aningkinanti

from view.view_nilai import cari,cetak,header,notoption
from view.input_nilai import inputan,ubah,hapus
header()
while True:

    c = input("\nSILAHKAN PILIH OPSI: ")

    # EXIT PROGRAM
    

    # PRINT DATA
    if c.lower() == 'l':
        cetak()

    # MENAMBAH DATA
    elif c.lower() == 't':
        inputan()

    # UBAH DATA
    elif c.lower() == 'u':
        ubah()

    # MENCARI DATA
    elif c.lower() == 'c':
        cari()

    # HAPUS DATA
    elif c.lower() == 'h':
        hapus()

    else:
        notoption()