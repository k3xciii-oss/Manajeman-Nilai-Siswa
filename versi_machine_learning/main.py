import json
import os
from versi_machine_learning.machineLearning import prediksi

def clear():
    os.system('cls' if os.name == 'nt' else 'clear')
    
def load():
    try:
        with open('db.json') as file:
            data = json.load(file)
            return data
    except (FileNotFoundError, json.JSONDecodeError):
        return []
    
def save_data(data):
    with open('db.json', 'w') as file:
        json.dump(data, file, indent=4)
    
def generate_id(data):
    if not data:
        return 1
    return data[-1]['id'] + 1

def add_data():
    data = load()
    while True:
        nama = input('Masukkan nama siswa: ').strip()
        if not nama:
            print('Nama Tidak boleh kosong!')
            continue
        if not nama.replace(' ', '').isalpha():
            print('Nama Harus Huruf Tidak Boleh angka!')
            continue
        break
    while True:
        kelas = input('Masukkan Kelas siswa: ').strip()
        if not kelas:
            print('Kelas tidak boleh Kosong!')
            continue
        break
    while True:
        try:
            kehadiran = int(input('Masukkan jumlah kehadiran siswa: '))
            if 0 <= kehadiran <= 100:
                break
            print('Kehadiran harus 0-100!')
        except ValueError:
            print('Masukkan angka!')
        
    daftar_nilai = []
    while True:
        try:
            mapel = str(input('Masukkan Nama Mapel(jika selesai ketik (selesai)): '))

            if mapel == 'selesai':
                if len(daftar_nilai) == 0:
                    print('Minimal harus ada 1 mapel!')
                    continue
                break
            
            if not mapel:
                print('Mapel tidak boleh kosong')
                continue
            if not mapel.replace(' ','').isalpha():
                print('Mapel Hanya boleh huruf')
                continue
        except ValueError:
            print('Tidak boleh ada angka atau selain huruf!')
            
        
        while True:
            try:
                nilai = int(input('Masukkan nilai dari Mapel: '))
                
                if 0 <= nilai <= 100:
                    break
                print('Nilai Harus 0-100')
            except ValueError:
                print('Masukkan angka')
        daftar_nilai.append({
            'mapel': mapel,
            'nilai': nilai
        })
        
    siswa = {
        'id': generate_id(data),
        'nama': nama,
        'kelas': kelas,
        'kehadiran': kehadiran,
        'nilai': daftar_nilai
    }
    data.append(siswa)
    
    save_data(data)
    
    print('\nData berhasil Ditambahkan')
def read_data():
    data = load()
    
    print(garis)
    print('Daftar Data Siswa')
    print(garis)
    if not data:
        print('=== Data belum ada ===')
        return
    for siswa in data:
        print(f'\nID: {siswa["id"]}')
        print(f'Nama: {siswa["nama"]}')
        print(f'Kelas: {siswa["kelas"]}')
        print(f'Kehadiran: {siswa["kehadiran"]}')
        print('Nilai: ')
        
        for nilai in siswa['nilai']:
            print(f'- Mapel: {nilai["mapel"]} : {nilai["nilai"]}')
    print('-'*30)
    
def update_data():
    data = load()
    
    if not data:
        print('Data masih kosong')
        return
    

    read_data()
    while True:
        try:
            id_siswa = int(input('\nMasukkan ID siswa: '))
            break
        except ValueError:
            print('ID harus angka!')
            
    ditemukan = False
    for siswa in data:
        if siswa['id'] == id_siswa:
            ditemukan = True
            print(f'\nSiswa ditemukan: {siswa["nama"]}')
            while True:
                mapel_update = input('Masukkan Mapel yang mau di update: ')
                ditemukan_mapel = False
                
                for nilai in siswa['nilai']:
                    if nilai['mapel'].lower() == mapel_update.lower():
                        ditemukan_mapel = True
                        break
                if ditemukan_mapel:
                    break
                print('Mapel tidak ditemukan')
                
                    
            for nilai in siswa['nilai']:
                if nilai['mapel'].lower() == mapel_update.lower():
                    while True:
                        try:
                            nilai_baru = int(input('Masukkan nilai baru: '))
                            if 0 <= nilai_baru <= 100:
                                break
                            print('Nilai Harus 0-100')
                        except ValueError:
                            print('Masukkan angka')
                            
                    nilai['nilai'] = nilai_baru
                    save_data(data)
                    print('\nNilai berhasil di update')
                    break

    if not ditemukan:
        print('\nID Siswa Tidak Ditemukan')
        input('Tekan Enter untuk lanjut...')
        
def delete_data():
    data = load()
    
    read_data()
    if not data:
        print('Data Masih kosong')
        return
    while True:
        try:
            id_hapus = int(input('\nMasukkan ID siswa: '))
            
            break
        except ValueError:
            print('ID harus angka')
    ditemukan = False
    for siswa in data:
        if siswa['id'] == id_hapus:
            ditemukan = True
            konfirmasi = input(f'Yakin ingin Mengahapus {siswa["nama"]}? (y/n)').lower()
            if konfirmasi == 'y':
                data.remove(siswa)
                save_data(data)
                print('\nData Siswa Berhasil di Hapus')
                return
            else:
                print('\n=== Penghapusan Dibatalkan ===')
                input('\nTekan Enter Untuk Melanjutkan...')
                return
    if not ditemukan:
        print('ID Siswa Tidak Ditemukan')
def hitung_rata(siswa):
    total = 0
    for nilai in siswa['nilai']:
        total += nilai['nilai']
    return total / len(siswa['nilai'])

def predict_lulus():
    data = load()
    while True:
        try:
            id_siswa = int(input('\nMasukkan ID siswa: '))
            break
        except ValueError:
            print('ID harus angka!')

    
    ditemukan = False
    for siswa in data:
        if siswa['id'] == id_siswa:
            ditemukan = True
            
            rata = hitung_rata(siswa)
            kategori_rata = ''
            kategori_kehadiran = ''
            print(garis)
            print(f'{prediksi(siswa["kehadiran"], rata)}')
            print(garis)
            print('Kehadiran: ', siswa['kehadiran'])
            print(f'Rata - rata: {rata:.1f}')
            print('\nFaktor Utama:')
            if rata >= 90:
                kategori_rata = 'Tinggi'
            elif rata >= 75:
                kategori_rata = 'Sedang'
            else:
                kategori_rata = 'Rendah'
            if siswa['kehadiran'] >= 85:
                kategori_kehadiran = 'Tinggi'
            elif siswa['kehadiran'] >= 75:
                kategori_kehadiran = 'Sedang'
            else:
                kategori_kehadiran = 'Rendah'
            print(f'- Kehadiran: {kategori_kehadiran}')
            print(f'- Nilai Rata - rata: {kategori_rata}')
    if not ditemukan:
        print('\nID Tidak ditemukan')
        input('Tekan Enter Untuk melanjutkan')

def cari_siswa():
    clear()
    data = load()
    
    if not data:
        print('Data masih kosong')
        return
    print(garis)
    print(''*10,'CARI SISWA',''*10)
    print(garis)
    pilihan_cari = input('\n1. Cari berdasarkan ID\n2. Cari Berdasarkan Nama \n3. Cari Berdsarkan kelas\npilih(1/2/3): ')
    if pilihan_cari == '1':
        while True:
            try:
                id_siswa = int(input('\nMasukkan ID siswa: '))
                break
            except ValueError:
                print('ID harus angka!')
                
        ditemukan = False
        for siswa in data:
            if siswa['id'] == id_siswa:
                ditemukan = True
                print(f'\nID: {siswa["id"]}')
                print(f'Nama: {siswa["nama"]}')
                print(f'Kelas: {siswa["kelas"]}')
                print(f'Kehadiran: {siswa["kehadiran"]}')
                print('Nilai: ')
                
                for nilai in siswa['nilai']:
                    print(f'- Mapel: {nilai["mapel"]} : {nilai["nilai"]}')
                print('-'*30)
                input('Tekan Enter...')
                
        if not ditemukan:
            print('ID Tidak Ditemukan!')
            input('Tekan Enter...')
            
    elif pilihan_cari == '2':
        while True:
            
            nama_cari = input('Masukkan nama yang di cari: ').strip()
            if not nama_cari:
                print('Nama Harus sesuai!')
                continue
            else:
                break
                
        ditemukan = False
        for siswa in data:
            if siswa['nama'].lower() == nama_cari.lower():
                ditemukan = True
                print(f'\nID: {siswa["id"]}')
                print(f'Nama: {siswa["nama"]}')
                print(f'Kelas: {siswa["kelas"]}')
                print(f'Kehadiran: {siswa["kehadiran"]}')
                print('Nilai: ')
                
                for nilai in siswa['nilai']:
                    print(f'- Mapel: {nilai["mapel"]} : {nilai["nilai"]}')
                print('-'*30)
                input('Tekan Enter...')
                
        if not ditemukan:
            print('Nama Tidak Ditemukan!')
            input('Tekan enter...')
    elif pilihan_cari == '3':
        while True:
            kelas_cari = input('Masukkan kelas yang di cari: ').strip()
            if not kelas_cari:
                print('Tidak Boleh kosong')
                continue
            else:
                break
        
        ditemukan = False    
        for siswa in data:
            if siswa['kelas'].lower() == kelas_cari.lower():
                ditemukan = True
                print(f'\nID: {siswa["id"]}')
                print(f'Nama: {siswa["nama"]}')
                print(f'Kelas: {siswa["kelas"]}')
                print(f'Kehadiran: {siswa["kehadiran"]}')
                print('Nilai: ')
                
                for nilai in siswa['nilai']:
                    print(f'- Mapel: {nilai["mapel"]} : {nilai["nilai"]}')
                print('-'*30)
                input('Tekan Enter...')
        if not ditemukan:
            print('Kelas Tidak Ditemukan!')
            input('Tekan Enter...')
    else:
        print('Pilihan Tidak Valid!') 
while True:
    clear()
    garis = '='*30
    print(garis)
    print('PROGRAM MANAJEMAN SISWA')
    print(garis)
    
    print('\n1. Tambahkan Data')
    print('2. Lihat Data')
    print('3. Update Data')
    print('4. Hapus Data')
    print('5. Prediksi lulus/tidak')
    print('6. Cari Siswa')
    print('7. Keluar Program')
    pilihan = input('Masukkan pilihan (1/2/3/4/5/6): ')
    
    if pilihan == '1':
        add_data()
    elif pilihan == '2':
        read_data()
        input('Tekan Enter Untuk Melanjutkan/Kembali...')
    elif pilihan == '3':
        update_data()
    elif pilihan == '4':
        delete_data()
    elif pilihan == '5':
        predict_lulus()
        input('Tekan Enter....')
        continue
    elif pilihan == '6':
        cari_siswa()
    elif pilihan == '7':
        break
    else:
        print('Pilihan Tidak Valid')
        input('Tekan Enter...')