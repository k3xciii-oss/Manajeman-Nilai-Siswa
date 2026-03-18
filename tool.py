from time import sleep
import db
import os

def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

def judul():
    garis = '==========================='
    print(garis)
    print('MANAJEMAN NILAI SISWA')
    print(garis)

def add():
    nama = input('Masukkan nama: ')
    kelas = input('Masukkan kelas: ')
    
    id_siswa = db.insert_data(nama,kelas)   
    
    
    while True:
        mapel = input('Masukkan mapel yang diinginkan (ketik (selesai) jika sudah: )')
        if mapel.lower() == 'selesai':
            break
        nilai = int(input(f'Masukkan nilai {mapel}: '))
        db.insert_nilai(id_siswa,mapel,nilai)

def cek():
    data = db.fetch_siswa_dengan_nilai()
    current_id = None
    for baris in data:
        id_siswa, nama, kelas, mapel, nilai = baris
        if id_siswa != current_id:
            if current_id is not None:
                print()
            print(f'Nama: {nama} | Kelas: {kelas}')
            print('NILAI: ')
            current_id = id_siswa
        if mapel is not None:
            print(f'- {mapel}: {nilai}')
    
    
    
def delete(nama):
    db.del_data(nama)
    print('Data berhasil dihapus')

def exit_program():
    print('Program Akan di hentikan')
    sleep(1)
    print('3...')
    sleep(1)
    print('2...')
    sleep(1)
    print('1...')
    sleep(1)
    print('program berhasil di hentikan')
    exit()


def start():
    while True:
        clear()
        judul()
        try:
            user_option = int(input(f'\n\nsilahkan pilih programnya:\n1.Tambah data siswa\n2.lihat data\n3.Hapus data siswa\n4.Keluar\n\nsilahkan pilih: '))
        except:
            print('Masukkan angka!')
            continue
        clear()
        if user_option == 1:
            add()
            input('Tekan enter untuk kembali ke menu...')
            clear()
            
        elif user_option == 2:
            cek()     
            input('Tekan enter untuk kembali ke menu...')
                  

        elif user_option == 3:
            cek()
            nama = input('Masukkan nama yang mau dihapus: ')
            delete(nama)
            input('Tekan enter untuk kembali ke menu...')
            
                
        elif user_option == 4:
           exit_program()
        else:
            print('Hanya boleh pilih (1/2/3/4/5)') 
            continue
