====|PROGRAM MANAJEMAN NILAI SISWA|====

Program berbasis python untuk mengelola data dan nilai siswa dengan menggunakan mysql

# FITUR:
1. Tambah data siswa
2. Tambah nilai siswa
3. Lihat data dan nilai siswa
4. Hapus data dan nilai siswa

# STRUKTUR FILE 

- FILE DB:
1. Menghubungkan dengan database Mysql ke python
2. berisi fungsi:
    - Insert Data() / memasukkan data siswa seperti, nama dan kelas, dari python ke database
    - Insert nilai() / memasukkan nilai siswa seperti, mapel dan nilai dari python ke database
    - Fetch_siswa_dengan_nilai() adalah fungsi untuk megambil data dan nilai siswa dari database
    - del_data() adalah fungsi untuk menghapus data dan nilai siswa hanya dengan memasukkan nama yang ingin di hapus dari database
- FILE TOOL:
1. Berisi program yang akan dijalankan yang terhubung dengan file DB dan digunakan untuk file utama yaitu, main.py
2. Berisi:
    - Fungsi clear() adalah fungsi untuk membersihkan terminal
    - Fungsi judul() adalah fungsi untuk menampilkan judul
    - Fungsi add() adalah fungsi untuk menambahkan data dan nilai siswa ke file DB yang langsung di kirim ke database
    - Fungsi cek() adalah fungsi untuk menampilkan data dan nilai siswa yang sudah di ambil fungsi fetch_siswa_dengan_nilai dari database
    - Fungsi delete() adalah fungsi untuk menghapus data dan nilai siswa yang dipilih user dan di ambil dari fungsi Del dari db
    - Fungsi exit_program() adalah fungsi untuk keluar dari program tersebut dengan hitungan mundur 3 detik
    - Fungsi start() berisi:
       - Program utama
       - Melakukan perulangan
       - Memanggil fungsi clear untuk membersihkan tampilan terminal agar lebih nyaman di pandang
       - Memanggil fungsi judul untuk menampilkan judul
       - Meminta user memilih program yang mau dijalankan, Jika user salah memasukkan pilihan maka akan di ulang lagi
       - Jika user memilih opsi pertama maka, akan menjalankan fungsi add(), yang bertugas untuk menambahkan data dan nilai siswa
       - Jika user memilih opsi kedua maka, akan menjalankan fungsi cek() untuk menampilkan semua data dan nilai siswa
       - Jika user memilih opsi ketiga maka, akan menjalankan fungsi cek() dulu untuk menampilkan semua data dan nilai siswa,
         lalu user diminta memasukkan nama yang ingin dihapus, dan menjalankan fungsi delete() yang diisi dengan nama yang mau dihapus
       - Jika user memilih opsi keempat maka, akan menjalankan fungsi exit_program() untuk keluar dari program nya
       - Jika user salah ketik/memilih opsi yang tidak ada di menu maka, akan disuruh untuk mengisi ulang pilihannya
- FILE MAIN:
1. Adalah tempat dimana menjalankan program yang sudah dibuat
2. Mengimport fungsi start() dari file tool.py
3. Memanggil fungsi start() yang dimasukkan ke dalam fungsi main
4. Memanggil fungsi main() yang sudah berisi fungsi start() untuk dijalankan

# CARA MENJALANKAN PROGRAM
1. Install library Mysql.connector di python dengan terminal
2. Set up database dengan cara:
    - Buat database kamu
    - Buat tabel di dalam database kamu
    - Untuk tabel_data isi dengan id_siswa,nama,kelas
    - Buat tabel_nilai lagi, isi dengan id_nilai,mapel,nilai
    - Lalu hubungkan kedua tabel tersebut
    - Jangan lupa untuk menyalakan database yang kamu buat menggunkan xampp, agar python bisa terhubung dengan database kamu 
3. Jalankan program yang di file main.py
