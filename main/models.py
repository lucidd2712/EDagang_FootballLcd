from django.db import models

class Product(models.Model):
    name = models.CharField(max_length=100)  # Nama item
    price = models.IntegerField()            # Harga item
    description = models.TextField()         # Deskripsi item
    thumbnail = models.URLField()            # URL gambar item
    category = models.CharField(max_length=50)  # Kategori item
    is_featured = models.BooleanField(default=False)  # Status unggulan

    def __str__(self):
        return self.name
