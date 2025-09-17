# from django.test import TestCase, Client
# from .models import News

from django.test import TestCase, Client
from django.contrib.auth.models import User
from main.models import Product
from django.contrib.staticfiles.testing import LiveServerTestCase
from django.contrib.auth.models import User
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class MainTest(TestCase):
    def setUp(self):
        # Buat user untuk relasi ke Product
        self.user = User.objects.create_user(username="testuser", password="password123")

    def test_main_url_is_exist(self):
        response = Client().get("/")
        self.assertEqual(response.status_code, 200)

    def test_main_using_home_template(self):
        response = Client().get("/")
        self.assertTemplateUsed(response, "home.html")

    def test_nonexistent_page(self):
        response = Client().get("/burhan_always_exists/")
        self.assertEqual(response.status_code, 404)

    def test_product_creation(self):
        product = Product.objects.create(
            user=self.user,
            name="Bola Adidas",
            price=500000,
            stock=10,
            description="Bola resmi Liga Champions",
            image_url="https://example.com/bola.jpg"
        )
        self.assertEqual(product.name, "Bola Adidas")
        self.assertEqual(product.price, 500000)
        self.assertEqual(product.stock, 10)
        self.assertEqual(product.user.username, "testuser")

    def test_product_default_values(self):
        product = Product.objects.create(
            user=self.user,
            name="Sepatu Nike",
            price=1200000,
            stock=5,
            description="Sepatu futsal original"
        )
        # Pastikan image_url bisa kosong
        self.assertIsNone(product.image_url)

    def test_str_method(self):
        product = Product.objects.create(
            user=self.user,
            name="Jersey Real Madrid",
            price=1500000,
            stock=3,
            description="Home jersey 2025"
        )
        self.assertEqual(str(product), "Jersey Real Madrid")



class ProductFunctionalTest(LiveServerTestCase):
    @classmethod
    def setUpClass(cls):
        super().setUpClass()
        # Pastikan chromedriver sesuai versi Chrome
        cls.browser = webdriver.Chrome()

    @classmethod
    def tearDownClass(cls):
        cls.browser.quit()
        super().tearDownClass()

    def setUp(self):
        self.browser.delete_all_cookies()

        # Buat user untuk setiap test
        self.test_user = User.objects.create_user(username="testuser", password="password123")

        # Login otomatis
        self.browser.get(f"{self.live_server_url}/login/")
        self.browser.find_element(By.NAME, "username").send_keys("testuser")
        self.browser.find_element(By.NAME, "password").send_keys("password123")
        self.browser.find_element(By.TAG_NAME, "form").submit()

        # Tunggu halaman utama muncul
        wait = WebDriverWait(self.browser, 10)
        self.h1_element = wait.until(
            EC.presence_of_element_located((By.TAG_NAME, "h1"))
        )

    def tearDown(self):
        self.browser.get("about:blank")

    def test_login_successful(self):
        self.assertIn("EDagang Football", self.h1_element.text)

        # Cek tombol logout muncul
        logout_button = self.browser.find_element(By.XPATH, "//button[contains(text(), 'Logout')]")
        self.assertTrue(logout_button.is_displayed())

    def test_create_product(self):
        # Pergi ke halaman tambah produk
        add_button = self.browser.find_element(By.PARTIAL_LINK_TEXT, "Tambah Produk")
        add_button.click()

        h1 = WebDriverWait(self.browser, 10).until(
            EC.presence_of_element_located((By.TAG_NAME, "h1"))
        )
        self.assertIn("Tambah Produk", h1.text)

        # Isi form produk
        self.browser.find_element(By.NAME, "name").send_keys("Test Bola")
        self.browser.find_element(By.NAME, "price").send_keys("250000")
        self.browser.find_element(By.NAME, "stock").send_keys("5")
        self.browser.find_element(By.NAME, "description").send_keys("Bola untuk pengujian selenium")
        self.browser.find_element(By.NAME, "image_url").send_keys("https://example.com/bola.jpg")
        self.browser.find_element(By.NAME, "name").submit()

        # Tunggu produk muncul di halaman utama
        WebDriverWait(self.browser, 10).until(
            EC.presence_of_element_located((By.PARTIAL_LINK_TEXT, "Test Bola"))
        )
        product_link = self.browser.find_element(By.PARTIAL_LINK_TEXT, "Test Bola")
        self.assertTrue(product_link.is_displayed())

    def test_product_detail_page(self):
        # Buat produk langsung di DB
        product = Product.objects.create(
            user=self.test_user,
            name="Detail Bola",
            price=100000,
            stock=2,
            description="Detail test bola"
        )

        # Buka halaman detail produk
        self.browser.get(f"{self.live_server_url}/product/{product.id}/")

        self.assertIn("Detail Bola", self.browser.page_source)
        self.assertIn("Detail test bola", self.browser.page_source)

    def test_logout(self):
        logout_button = self.browser.find_element(By.XPATH, "//button[contains(text(), 'Logout')]")
        logout_button.click()

        h1 = WebDriverWait(self.browser, 10).until(
            EC.presence_of_element_located((By.TAG_NAME, "h1"))
        )
        self.assertIn("Login", h1.text)

    def test_filter_main_page(self):
        # Buat beberapa produk
        Product.objects.create(
            user=self.test_user,
            name="My Test Product",
            price=50000,
            stock=10,
            description="Produk dari saya"
        )
        Product.objects.create(
            user=self.test_user,
            name="Other Product",
            price=75000,
            stock=5,
            description="Produk lain"
        )

        # Filter All
        all_button = self.browser.find_element(By.XPATH, "//button[contains(text(), 'All Articles')]")
        all_button.click()
        WebDriverWait(self.browser, 10).until(
            EC.presence_of_element_located((By.PARTIAL_LINK_TEXT, "My Test Product"))
        )
        self.assertIn("My Test Product", self.browser.page_source)
        self.assertIn("Other Product", self.browser.page_source)

        # Filter My
        my_button = self.browser.find_element(By.XPATH, "//button[contains(text(), 'My Articles')]")
        my_button.click()
        WebDriverWait(self.browser, 10).until(
            EC.presence_of_element_located((By.PARTIAL_LINK_TEXT, "My Test Product"))
        )
        self.assertIn("My Test Product", self.browser.page_source)
        self.assertIn("Other Product", self.browser.page_source)



# class ProductFunctionalTest(LiveServerTestCase):
#     @classmethod
#     def setUpClass(cls):
#         super().setUpClass()
#         cls.browser = webdriver.Chrome()

#     @classmethod
#     def tearDownClass(cls):
#         super().tearDownClass()
#         cls.browser.quit()

#     def setUp(self):
#         self.browser.delete_all_cookies()

#     def tearDown(self):
#         self.browser.get("about:blank")

#     def register_user(self, username="testuser", password="password123"):
#         """Helper to register a new user via UI"""
#         self.browser.get(f"{self.live_server_url}/register/")
#         self.browser.find_element(By.NAME, "username").send_keys(username)
#         self.browser.find_element(By.NAME, "password1").send_keys(password)
#         self.browser.find_element(By.NAME, "password2").send_keys(password)
#         self.browser.find_element(By.NAME, "password2").submit()

#         # tunggu redirect ke login
#         WebDriverWait(self.browser, 10).until(
#             EC.text_to_be_present_in_element((By.TAG_NAME, "h1"), "Login")
#         )

#     def login_user(self, username="testuser", password="password123"):
#         """Helper to login user via UI"""
#         self.browser.get(f"{self.live_server_url}/login/")
#         self.browser.find_element(By.NAME, "username").send_keys(username)
#         self.browser.find_element(By.NAME, "password").send_keys(password)
#         self.browser.find_element(By.NAME, "password").submit()

#         WebDriverWait(self.browser, 10).until(
#             EC.presence_of_element_located((By.TAG_NAME, "h1"))
#         )

#     def test_register_and_login(self):
#         self.register_user()
#         self.login_user()
#         h1_element = self.browser.find_element(By.TAG_NAME, "h1")
#         self.assertIn("EDagang Football", h1_element.text)

#     def test_create_product(self):
#         self.register_user()
#         self.login_user()

#         add_button = self.browser.find_element(By.PARTIAL_LINK_TEXT, "Tambah Produk")
#         add_button.click()

#         self.browser.find_element(By.NAME, "name").send_keys("Test Bola")
#         self.browser.find_element(By.NAME, "price").send_keys("250000")
#         self.browser.find_element(By.NAME, "stock").send_keys("5")
#         self.browser.find_element(By.NAME, "description").send_keys("Bola selenium")
#         self.browser.find_element(By.NAME, "image_url").send_keys("https://example.com/bola.jpg")
#         self.browser.find_element(By.NAME, "image_url").submit()

#         WebDriverWait(self.browser, 10).until(
#             EC.presence_of_element_located((By.PARTIAL_LINK_TEXT, "Test Bola"))
#         )
#         self.assertTrue(self.browser.find_element(By.PARTIAL_LINK_TEXT, "Test Bola").is_displayed())

#     def test_register_page(self):
#         # Test register functionality
#         self.browser.get(f"{self.live_server_url}/register/")

#         h1_element = self.browser.find_element(By.TAG_NAME, "h1")
#         self.assertEqual(h1_element.text, "Register")

#         # Fill register form
#         username_input = self.browser.find_element(By.NAME, "username")
#         password1_input = self.browser.find_element(By.NAME, "password1")
#         password2_input = self.browser.find_element(By.NAME, "password2")

#         username_input.send_keys("newuser")
#         password1_input.send_keys("complexpass123")
#         password2_input.send_keys("complexpass123")
#         password2_input.submit()

#         # Check redirect to login page
#         wait = WebDriverWait(self.browser, 10)
#         wait.until(EC.text_to_be_present_in_element((By.TAG_NAME, "h1"), "Login"))
#         login_h1 = self.browser.find_element(By.TAG_NAME, "h1")
#         self.assertEqual(login_h1.text, "Login")

#     def test_login_page(self):
#         self.login_user()

#         wait = WebDriverWait(self.browser, 10)
#         wait.until(EC.presence_of_element_located((By.TAG_NAME, "h1")))
#         h1_element = self.browser.find_element(By.TAG_NAME, "h1")
#         self.assertEqual(h1_element.text, "EDagang Football L")

#         logout_button = self.browser.find_element(By.XPATH, "//button[contains(text(), 'Logout')]")
#         self.assertTrue(logout_button.is_displayed())

#     def test_create_product(self):
#         self.login_user()
#         # Go to create product page
#         add_button = self.browser.find_element(By.PARTIAL_LINK_TEXT, "Tambah Produk")
#         add_button.click()

#         h1_element = self.browser.find_element(By.TAG_NAME, "h1")
#         self.assertEqual(h1_element.text, "Tambah Produk")

#         # Fill form
#         name_input = self.browser.find_element(By.NAME, "name")
#         price_input = self.browser.find_element(By.NAME, "price")
#         stock_input = self.browser.find_element(By.NAME, "stock")
#         description_input = self.browser.find_element(By.NAME, "description")
#         image_url_input = self.browser.find_element(By.NAME, "image_url")

#         name_input.send_keys("Test Bola")
#         price_input.send_keys("250000")
#         stock_input.send_keys("5")
#         description_input.send_keys("Bola untuk pengujian selenium")
#         image_url_input.send_keys("https://example.com/bola.jpg")

#         name_input.submit()

#         # Check if returned to main page and product appears
#         wait = WebDriverWait(self.browser, 10)
#         wait.until(EC.presence_of_element_located((By.PARTIAL_LINK_TEXT, "Test Bola")))
#         product_title = self.browser.find_element(By.PARTIAL_LINK_TEXT, "Test Bola")
#         self.assertTrue(product_title.is_displayed())

#     def test_product_detail_page(self):
#         product = Product.objects.create(
#             user=self.test_user,
#             name="Detail Bola",
#             price=100000,
#             stock=2,
#             description="Detail test bola"
#         )

#         # Harus login dulu
#         self.login_user()

#         # Baru buka halaman detail produk
#         self.browser.get(f"{self.live_server_url}/product/{product.id}/")

#         self.assertIn("Detail Bola", self.browser.page_source)
#         self.assertIn("Detail test bola", self.browser.page_source)


#     def test_logout(self):
#         self.login_user()
#         logout_button = self.browser.find_element(By.XPATH, "//button[contains(text(), 'Logout')]")
#         logout_button.click()

#         wait = WebDriverWait(self.browser, 10)
#         wait.until(EC.text_to_be_present_in_element((By.TAG_NAME, "h1"), "Login"))
#         h1_element = self.browser.find_element(By.TAG_NAME, "h1")
#         self.assertEqual(h1_element.text, "Login")

#     def test_filter_main_page(self):
#         from main.models import Product
#         Product.objects.create(
#             user=self.test_user,
#             name="My Test Product",
#             price=50000,
#             stock=10,
#             description="Produk dari saya"
#         )
#         Product.objects.create(
#             user=self.test_user,
#             name="Other Product",
#             price=75000,
#             stock=5,
#             description="Produk lain"
#         )

#         self.login_user()

#         # Filter All
#         all_button = self.browser.find_element(By.XPATH, "//button[contains(text(), 'All Articles')]")
#         all_button.click()
#         self.assertIn("My Test Product", self.browser.page_source)
#         self.assertIn("Other Product", self.browser.page_source)

#         # Filter My
#         my_button = self.browser.find_element(By.XPATH, "//button[contains(text(), 'My Articles')]")
#         my_button.click()
#         self.assertIn("My Test Product", self.browser.page_source)

