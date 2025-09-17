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







Tugas 4 

(Nomor 1) Apa itu Django AuthenticationForm? Jelaskan juga kelebihan dan kekurangannya.
Django AuthenticationForm adalah sebuah form bawaan dari framework Django yang dirancang khusus untuk menangani proses autentikasi pengguna, yaitu login. Form ini disediakan oleh modul django.contrib.auth.forms dan secara default sudah memiliki field untuk username dan password, serta melakukan validasi data secara otomatis. Dengan menggunakan AuthenticationForm, pengembang tidak perlu membuat logika autentikasi dari nol, karena form ini sudah menggabungkan validasi input, pengecekan keberadaan pengguna, dan pemeriksaan kecocokan password. Kelebihan utama AuthenticationForm adalah kemudahannya untuk digunakan dan integrasinya yang langsung dengan sistem autentikasi Django. Form ini menghemat waktu pengembangan karena semua proses penting, seperti validasi password dan pengecekan apakah user aktif, sudah ditangani. Selain itu, form ini aman karena mengikuti praktik standar Django, termasuk perlindungan terhadap serangan brute-force atau manipulasi data login. Namun, AuthenticationForm juga memiliki beberapa keterbatasan. Form ini hanya menyediakan autentikasi berbasis username dan password, sehingga tidak mendukung autentikasi multi-faktor atau metode login alternatif seperti token atau OAuth secara langsung. Selain itu, tampilannya default cukup sederhana, sehingga jika ingin desain form yang lebih kustom atau menambahkan field tambahan, pengembang harus melakukan override atau membuat subclass sendiri. Secara keseluruhan, AuthenticationForm sangat berguna untuk kasus login standar dan cepat, tetapi perlu penyesuaian jika aplikasi membutuhkan fitur autentikasi yang lebih kompleks.



(Nomor 2) Apa perbedaan antara autentikasi dan otorisasi? Bagaiamana Django mengimplementasikan kedua konsep tersebut?
Autentikasi dan otorisasi adalah dua konsep penting dalam keamanan aplikasi, tetapi memiliki peran yang berbeda. Autentikasi adalah proses untuk memverifikasi identitas pengguna, memastikan bahwa seseorang yang mencoba mengakses sistem benar-benar merupakan pengguna yang sah. Biasanya, autentikasi dilakukan melalui kombinasi username dan password, meskipun metode lain seperti token, OAuth, atau autentikasi multi-faktor juga dapat digunakan. Sebaliknya, otorisasi adalah proses menentukan hak atau izin pengguna setelah identitasnya diverifikasi, yaitu memutuskan sumber daya atau fungsi apa saja yang boleh diakses oleh pengguna tersebut. Dengan kata lain, autentikasi menjawab pertanyaan "Siapa kamu?", sedangkan otorisasi menjawab "Apa yang boleh kamu lakukan?". Dalam Django, kedua konsep ini diimplementasikan secara terpisah tetapi saling terkait. Django menyediakan sistem autentikasi bawaan melalui modul django.contrib.auth, yang menangani login pengguna menggunakan form standar seperti AuthenticationForm serta memverifikasi kredensial melalui model User. Setelah pengguna berhasil diautentikasi, Django menggunakan sistem izin (permissions) dan grup untuk mengatur otorisasi. Setiap model dapat memiliki izin tertentu, dan pengguna atau grup pengguna dapat diberikan hak akses spesifik. Dengan kombinasi ini, Django memungkinkan pengembang untuk memastikan bahwa hanya pengguna yang sah yang dapat mengakses sistem (autentikasi) dan bahwa mereka hanya bisa melakukan tindakan yang sesuai dengan haknya (otorisasi). Sistem ini membuat pengelolaan keamanan lebih terstruktur dan mudah diterapkan di berbagai level aplikasi.



(Nomor 3) Apa saja kelebihan dan kekurangan session dan cookies dalam konteks menyimpan state di aplikasi web?
Dalam konteks menyimpan state di aplikasi web, session dan cookies merupakan dua mekanisme yang sering digunakan, masing-masing memiliki kelebihan dan kekurangan. Session menyimpan data di sisi server dan hanya menyimpan identifier unik di browser pengguna, sehingga informasi sensitif seperti data login atau preferensi pengguna lebih aman dari akses pihak ketiga. Kelebihan lainnya adalah ukurannya tidak terbatas seperti cookies, dan mudah diatur untuk kadaluarsa secara otomatis saat sesi berakhir. Namun, kelemahannya adalah penggunaan session memerlukan penyimpanan di server, sehingga jika jumlah pengguna sangat banyak, konsumsi memori server bisa meningkat. Selain itu, session hanya berlaku selama koneksi pengguna aktif dan hilang ketika browser ditutup, kecuali diatur persistennya. Di sisi lain, cookies menyimpan data langsung di sisi klien, sehingga server tidak perlu menyimpan state untuk setiap pengguna, mengurangi beban server dan memungkinkan informasi tetap tersedia walaupun browser ditutup, selama masa kadaluarsa belum habis. Kekurangan cookies adalah ukurannya terbatas (biasanya sekitar 4 KB), dan data yang disimpan lebih rentan terhadap manipulasi atau pencurian jika tidak dienkripsi atau diberi tanda aman. Selain itu, cookies dikirimkan ke server setiap kali ada request, yang bisa menambah overhead jaringan jika ukurannya besar. Secara ringkas, session lebih aman dan fleksibel untuk data sensitif, sementara cookies lebih ringan dan cocok untuk data sederhana yang perlu disimpan di sisi klien.



(Nomor 4) Apakah penggunaan cookies aman secara default dalam pengembangan web, atau apakah ada risiko potensial yang harus diwaspadai? Bagaimana Django menangani hal tersebut?
Penggunaan cookies dalam pengembangan web tidak sepenuhnya aman secara default karena data yang tersimpan di sisi klien dapat diakses, dimodifikasi, atau dicuri oleh pihak ketiga jika tidak dikelola dengan baik. Risiko yang paling umum termasuk pencurian sesi (session hijacking), manipulasi data cookie, serta serangan cross-site scripting (XSS) yang memungkinkan penyerang membaca atau mengubah isi cookie. Oleh karena itu, penting untuk selalu menandai cookies sebagai HttpOnly, sehingga tidak dapat diakses melalui JavaScript, serta menggunakan atribut Secure agar cookie hanya dikirim melalui koneksi HTTPS. Selain itu, penentuan masa kadaluarsa dan penggunaan tanda digital atau enkripsi juga dapat menambah keamanan cookies. Django menangani potensi risiko ini dengan menyediakan mekanisme yang aman secara default untuk cookies yang digunakan dalam session dan autentikasi. Misalnya, cookie sesi (sessionid) secara otomatis ditandai sebagai HttpOnly, sehingga tidak dapat diakses melalui skrip di browser. Django juga mendukung pengaturan SESSION_COOKIE_SECURE untuk memastikan cookie hanya dikirim melalui HTTPS, serta SESSION_COOKIE_AGE untuk menentukan durasi hidup sesi. Dengan konfigurasi ini, Django membantu pengembang meminimalkan risiko terkait cookies, meskipun tetap disarankan untuk selalu memeriksa dan menyesuaikan pengaturan keamanan sesuai kebutuhan aplikasi.



(Nomor 5) Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas secara step-by-step (bukan hanya sekadar mengikuti tutorial).
Saya melaksanakan tugas ini dengan penuh seksama dan perhatian terhadap setiap detail. Pertama-tama, saya mengikuti tutorial secara menyeluruh, tidak hanya sekadar menyalin langkah-langkahnya, tetapi juga merenungkan alasan di balik setiap langkah dan bagaimana mekanismenya bekerja. Dari proses ini, saya memahami bahwa tugas saya mencakup pembuatan fitur login, logout, dan register. Berdasarkan pemahaman tersebut, saya kemudian mengimplementasikan fitur-fitur tersebut, membuat tiga akun pengguna, dan mencoba semua fungsinya hingga berhasil berjalan sesuai yang diharapkan. Setelah memastikan bahwa sistem login, logout, dan register berfungsi dengan baik, saya melanjutkan dengan membuat test case menggunakan Selenium. Langkah ini saya lakukan untuk memastikan bahwa program saya tidak hanya berjalan, tetapi juga aman dan andal, sehingga setiap fungsi dapat diuji secara otomatis dan hasilnya dapat dipertanggungjawabkan.