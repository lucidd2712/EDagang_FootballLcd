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
















Tugas 3
(nomor 1) Jelaskan mengapa kita memerlukan data delivery dalam pengimplementasian sebuah platform?
Kita memerlukan data delivery dalam pengimplementasian sebuah platform karena proses ini memastikan bahwa data yang dibutuhkan dapat berpindah dengan cepat, aman, dan tepat sasaran dari satu sistem ke sistem lainnya. Tanpa mekanisme pengiriman data yang baik, informasi yang dihasilkan oleh platform tidak akan dapat dimanfaatkan secara optimal oleh pengguna maupun layanan lain yang saling terhubung. Data delivery juga berperan penting dalam menjaga konsistensi, keakuratan, serta keterkinian data sehingga keputusan yang diambil berdasarkan data tersebut lebih relevan dan dapat dipertanggungjawabkan. Selain itu, dalam konteks platform yang bersifat real-time atau melibatkan banyak pengguna sekaligus, data delivery membantu menjaga performa sistem agar tetap responsif dan mendukung pengalaman pengguna yang lebih baik. Dengan kata lain, data delivery adalah fondasi utama yang memungkinkan sebuah platform berfungsi secara efektif, terintegrasi, dan scalable.


(nomor 2) Menurutmu, mana yang lebih baik antara XML dan JSON? Mengapa JSON lebih populer dibandingkan XML?
JSON lebih populer dibandingkan XML karena formatnya yang lebih sederhana, ringkas, dan mudah dipahami, baik oleh manusia maupun mesin. Struktur JSON berbasis key–value membuatnya langsung cocok dengan bahasa pemrograman modern, sehingga proses parsing dan integrasi data menjadi lebih cepat tanpa membutuhkan banyak konfigurasi tambahan. Selain itu, ukuran JSON yang lebih kecil membuat proses pertukaran data lebih efisien, terutama untuk aplikasi berbasis web dan mobile yang membutuhkan kecepatan. Sementara XML memiliki kelebihan dalam hal fleksibilitas dan kemampuan mendeskripsikan data dengan tag yang kaya, sintaksnya cenderung panjang dan kompleks. Oleh karena itu, JSON lebih banyak dipilih dalam pengembangan platform modern karena lebih praktis, efisien, dan sesuai dengan kebutuhan komunikasi data di era digital saat ini.


(nomor 3) Jelaskan fungsi dari method is_valid() pada form Django dan mengapa kita membutuhkan method tersebut?
Method is_valid() pada form Django berfungsi untuk melakukan validasi terhadap data yang dikirimkan melalui form. Saat pengguna mengisi dan mengirimkan data, Django akan memeriksa apakah data tersebut sesuai dengan aturan atau constraint yang telah ditentukan pada form maupun model terkait, misalnya tipe data, panjang karakter, keharusan mengisi field tertentu, atau aturan khusus lain yang didefinisikan. Jika semua aturan validasi terpenuhi, maka is_valid() akan mengembalikan nilai True, dan data form bisa diproses lebih lanjut, misalnya disimpan ke database. Sebaliknya, jika ada kesalahan, is_valid() mengembalikan False dan Django otomatis menyediakan pesan error yang dapat ditampilkan kembali kepada pengguna. Dengan demikian, method ini sangat penting karena membantu menjaga integritas data, mencegah terjadinya error atau data tidak valid yang masuk ke sistem, serta meningkatkan pengalaman pengguna dengan memberikan umpan balik langsung saat terjadi kesalahan input.


(nomor 4)Mengapa kita membutuhkan csrf_token saat membuat form di Django? Apa yang dapat terjadi jika kita tidak menambahkan csrf_token pada form Django? Bagaimana hal tersebut dapat dimanfaatkan oleh penyerang?
Kita membutuhkan csrf_token saat membuat form di Django karena token ini berfungsi sebagai lapisan keamanan tambahan untuk mencegah serangan Cross-Site Request Forgery (CSRF). CSRF adalah jenis serangan di mana penyerang mencoba memanipulasi pengguna agar tanpa sadar mengirimkan request berbahaya ke server, misalnya dengan cara mengklik tautan atau mengisi form palsu, sehingga server mengira request tersebut berasal dari pengguna yang sah. Dengan adanya csrf_token, setiap form yang dikirim harus menyertakan token unik yang hanya valid untuk sesi pengguna tersebut. Django akan memverifikasi token ini sebelum memproses request, sehingga request palsu yang dibuat penyerang akan ditolak. Jika kita tidak menambahkan csrf_token pada form Django, maka aplikasi menjadi rentan terhadap serangan CSRF. Penyerang dapat memanfaatkan kelemahan ini, misalnya dengan membuat halaman berbahaya yang secara otomatis mengirim request POST ke aplikasi target menggunakan akun pengguna yang sedang login. Akibatnya, penyerang bisa melakukan tindakan serius seperti mengubah data pengguna, menghapus data, hingga melakukan transaksi tanpa sepengetahuan korban. Dengan kata lain, tanpa csrf_token, integritas dan keamanan data dalam aplikasi bisa dengan mudah dikompromikan.


(nomor 5) Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas secara step-by-step (bukan hanya sekadar mengikuti tutorial).
Dalam mengimplementasikan checklist tersebut, langkah pertama yang saya lakukan adalah memastikan model sudah lengkap dengan field yang dibutuhkan dan melakukan migrasi agar database sinkron. Setelah itu, saya membuat ModelForm untuk mempermudah proses input data sekaligus memastikan validasi berjalan otomatis. Selanjutnya, saya membuat view create_product yang menggunakan method is_valid() untuk mengecek data sebelum disimpan, dan setelah berhasil data akan diarahkan kembali ke halaman utama agar tidak terjadi duplikasi data saat pengguna melakukan refresh. Halaman utama (show_main) kemudian saya rancang untuk menampilkan daftar produk dengan tombol Add yang mengarah ke form penambahan data, serta tombol Detail untuk setiap produk yang menuju halaman detail (show_product) menggunakan get_object_or_404 agar lebih aman. Selain itu, saya menambahkan empat fungsi baru untuk mendukung data delivery, yaitu show_json, show_xml, show_json_by_id, dan show_xml_by_id dengan memanfaatkan serializers.serialize untuk mengubah queryset menjadi format JSON maupun XML. Saya juga menyiapkan routing di urls.py dengan nama yang konsisten agar bisa dipanggil melalui {% url %} di template. Pada bagian template, saya menggunakan home.html sebagai kerangka utama dan menambahkan {% csrf_token %} pada setiap form untuk mencegah serangan CSRF. Setelah semua fungsi selesai, saya menguji setiap fitur, mulai dari menambah data, melihat detail, hingga mengakses data dalam format JSON dan XML melalui endpoint yang sudah disiapkan. Dengan langkah-langkah ini, implementasi checklist tidak hanya sekadar mengikuti tutorial, tetapi juga mempertimbangkan keamanan, konsistensi, serta kejelasan alur aplikasi.


(nomor 6)Apakah ada feedback untuk asdos di tutorial 2 yang sudah kalian kerjakan?
Semua asisten dosen sangat baik dalam memberikan bimbingan. Meskipun pertemuan dilakukan secara online, mereka tetap merespons dengan baik setiap pertanyaan yang diajukan. Selain itu, mereka juga membantu saya ketika mengalami kesulitan dan memberikan arahan dalam memecahkan masalah, sehingga saya dapat menyelesaikan tutorial dengan baik serta memahami cara mengimplementasikannya.


# Dokumentasi Tugas 3

https://www.canva.com/design/DAGzJ7Jg1As/3r8d0ElLRKQPejgKpOaaYw/edit?utm_content=DAGzJ7Jg1As&utm_campaign=designshare&utm_medium=link2&utm_source=sharebutton


