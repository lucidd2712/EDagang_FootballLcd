from django.db import models # type: ignore

class Product(models.Model):
    CATEGORY_CHOICES = [
        ('jersey', 'Jersey'),
        ('shoes', 'Shoes'),
        ('ball', 'Ball'),
        ('accessory', 'Accessory'),
        ('other', 'Other'),
    ]

    name = models.CharField(max_length=255)
    price = models.IntegerField()
    description = models.TextField()
    thumbnail = models.URLField(blank=True, null=True)
    category = models.CharField(max_length=20, choices=CATEGORY_CHOICES, default='other')
    is_featured = models.BooleanField(default=False)

    # Tambahan opsional
    stock = models.PositiveIntegerField(default=0)
    brand = models.CharField(max_length=100, blank=True, null=True)

    def __str__(self):
        return self.name
