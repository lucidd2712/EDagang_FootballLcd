(Nomor 1)Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas secara step-by-step (bukan hanya sekadar mengikuti tutorial).

Saya memulai dengan membuat model Product di models.py untuk mendefinisikan struktur data produk di database, termasuk field seperti nama, harga, deskripsi, thumbnail, kategori, dan apakah produk ditampilkan sebagai featured. Setelah itu, saya membuat view di views.py yang bertugas mengambil data dari model menggunakan ORM Django dan mengirimkannya ke template HTML. Template HTML menggunakan perulangan untuk menampilkan data produk. Selanjutnya, saya menambahkan path di urls.py agar URL yang dikunjungi client mengarah ke view yang sesuai. Setelah semua kode siap, saya menjalankan migrasi database dengan perintah makemigrations dan migrate untuk membuat tabel dan menyimpan data. Terakhir, saya menjalankan server dengan runserver sehingga halaman web dapat diakses oleh client dan produk dapat ditampilkan.


(Nomor 2)Buatlah bagan yang berisi request client ke web aplikasi berbasis Django beserta responnya dan jelaskan pada bagan tersebut kaitan antara urls.py, views.py, models.py, dan berkas html.
gambar ada di submission 
Ketika client mengakses URL, Django pertama-tama mengecek urls.py untuk menentukan view mana yang harus dipanggil. View di views.py kemudian mengambil data dari database melalui model di models.py dan memprosesnya sesuai kebutuhan. Data yang diperoleh kemudian dikirim ke template HTML untuk dirender menjadi halaman web. Template HTML menampilkan data kepada client sebagai response HTTP. Jadi, urls.py mengarahkan request, views.py memproses logika dan data, models.py berinteraksi dengan database, dan template HTML menampilkan hasilnya ke pengguna.

(Nomor 3)Jelaskan peran settings.py dalam proyek Django!

settings.py berfungsi sebagai pusat konfigurasi proyek Django. Berkas ini menyimpan pengaturan database, aplikasi yang diinstal, lokasi template, file statis, konfigurasi keamanan, dan opsi lain yang memengaruhi seluruh proyek. Semua komponen Django, termasuk model, view, dan template, bergantung pada pengaturan ini agar dapat bekerja sesuai kebutuhan proyek.


(Nomor 4)Bagaimana cara kerja migrasi database di Django?

Migrasi database di Django bekerja dengan mendeteksi perubahan pada model. Ketika model dibuat atau diubah, perintah makemigrations menghasilkan file migrasi yang berisi instruksi perubahan struktur database. Selanjutnya, perintah migrate mengeksekusi file migrasi tersebut sehingga tabel di database dibuat atau diperbarui sesuai definisi model. Dengan cara ini, Django menjaga konsistensi antara kode model dan struktur database.


(Nomor 5)Menurut Anda, dari semua framework yang ada, mengapa framework Django dijadikan permulaan pembelajaran pengembangan perangkat lunak?

Django dipilih sebagai framework awal karena menyediakan banyak fitur built-in, seperti ORM, admin panel, autentikasi, dan templating, sehingga mahasiswa dapat fokus pada logika aplikasi tanpa membangun semuanya dari awal. Struktur proyek yang jelas memisahkan apps, models, views, dan templates memudahkan pemahaman alur kerja. Selain itu, Django memiliki fitur keamanan bawaan dan dokumentasi lengkap, yang membuatnya cocok untuk pemula belajar full-stack web development.


(Nomor 6)Apakah ada feedback untuk asisten dosen tutorial 1 yang telah kamu kerjakan sebelumnya?
Tutorial sudah cukup jelas dan mudah diikuti karena disertai contoh langsung yang dapat dijalankan.