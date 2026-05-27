import json
import os

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
        'nilai': daftar_nilai
    }
    data.append(siswa)
    
    save_data(data)
    
    print('\nData berhasil Ditambahkan')
def read_data():
    data = load()
    
    print('\n',garis)
    print('Daftar Data Siswa')
    print(garis)
    if not data:
        print('=== Data belum ada ===')
        return
    for siswa in data:
        print(f'\nID: {siswa["id"]}')
        print(f'Nama: {siswa["nama"]}')
        print(f'Kelas: {siswa["kelas"]}')
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
                    if nilai['mapel'] == mapel_update:
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
            
    for siswa in data:
        if siswa['id'] == id_hapus:
            konfirmasi = input(f'Yakin ingin Mengahapus {siswa["nama"]}? (y/n)').lower()
            if konfirmasi == 'y':
                data.remove(siswa)

                save_data(data)

                print('\nData Siswa Berhasil di Hapus')
                return
            else:
                print('\n=== Penghapusan Dibatalkan ===')
                input('\nTekan Enter Untuk Melanjutkan...')
    print('ID Siswa Tidak Ditemukan')      
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
    print('5. Keluar Program')
    
    pilihan = input('Masukkan pilihan (1/2/3/4/5): ')
    
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
        break
    else:
        print('Pilihan Tidak Valid')
        input('Tekan Enter...')
