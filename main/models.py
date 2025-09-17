from django.db import models
from django.contrib.auth.models import User

class Product(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    name = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=12, decimal_places=2)
    stock = models.IntegerField()
    description = models.TextField()
    image_url = models.URLField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
    


# contoh
# class News(models.Model):
#     CATEGORY_CHOICES = [
#         ('transfer', 'Transfer'),
#         ('update', 'Update'),
#         ('exclusive', 'Exclusive'),
#         ('match', 'Match'),
#         ('rumor', 'Rumor'),
#         ('analysis', 'Analysis'),
#     ]
    
#     id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
#     user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)  # 👉 tambahkan ini
#     title = models.CharField(max_length=255)
#     content = models.TextField()
#     category = models.CharField(max_length=20, choices=CATEGORY_CHOICES, default='update')
#     thumbnail = models.URLField(blank=True, null=True)
#     news_views = models.PositiveIntegerField(default=0)
#     created_at = models.DateTimeField(auto_now_add=True)
#     is_featured = models.BooleanField(default=False)
    
#     def __str__(self):
#         return self.title
    
#     @property
#     def is_news_hot(self):
#         return self.news_views > 20
        
#     def increment_views(self):
#         self.news_views += 1
#         self.save()
