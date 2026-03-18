import mysql.connector

db = mysql.connector.connect (
    host='localhost',
    user='root',
    password='',
    database='data_siswa'
)

def insert_data(nama,kelas):
    cursor = db.cursor()
    cursor.execute("INSERT INTO tbl_data (nama, kelas) VALUES (%s,%s)", (nama,kelas))
    db.commit()
    return cursor.lastrowid
        
def insert_nilai(id_siswa,mapel,nilai):
    cursor = db.cursor()
    cursor.execute("INSERT INTO tbl_nilai (id_siswa,mapel,nilai) VALUES (%s,%s,%s)", (id_siswa,mapel,nilai))
    db.commit()
    
    if cursor.rowcount > 0:
        print('\nData berhasil ditambahkan\n')
    else:
        print('\nGagal insert data\n')
    
    
def fetch_siswa_dengan_nilai():
    cursor = db.cursor()
    cursor.execute(" SELECT s.id_siswa, s.nama, s.kelas, n.mapel, n.nilai FROM tbl_data s LEFT JOIN tbl_nilai  n ON s.id_siswa = n.id_siswa ORDER BY s.id_siswa")
    return cursor.fetchall()

def del_data(nama):
    cursor = db.cursor()
    cursor.execute('SELECT id_siswa FROM  tbl_data WHERE nama=%s', (nama,))
    result = cursor.fetchone()
    if result is None:
        print('data tidak ditemukan')
        return
    id_siswa = result[0]
    
    #hapus seluruh nilai siswa
    cursor.execute('DELETE FROM tbl_nilai WHERE id_siswa=%s', (id_siswa,))
    #hapus data siswa
    cursor.execute('DELETE FROM tbl_data WHERE id_siswa=%s', (id_siswa,))
    
    db.commit()
    print(f'Data siswa {nama} berhasil di hapus')