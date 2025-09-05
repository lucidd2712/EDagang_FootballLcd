from django.shortcuts import render
from django.http import HttpResponse
from .models import Product

def show_home(request):
    products = Product.objects.all()  # ambil semua produk dari database
    context = {
        'app_name': 'EDagang Football Lucid',
        'student_name': 'Gilang Adjie Saputra',
        'student_class': 'PBP C',
        'products': products, 
    }
    return render(request, "home.html", context)
