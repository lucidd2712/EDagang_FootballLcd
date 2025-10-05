from django.shortcuts import render, redirect, get_object_or_404
from main.forms import ProductForm
from main.models import Product
from django.http import HttpResponse
from django.core import serializers
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
import datetime
from django.http import HttpResponseRedirect
from django.urls import reverse


from django.http import JsonResponse
from django.views.decorators.http import require_http_methods
from django.views.decorators.csrf import csrf_exempt
from django.forms.models import model_to_dict
from django.contrib.auth.models import User
from django.middleware.csrf import get_token




@login_required(login_url='/login')
def show_main(request, category=None):
    filter_type = request.GET.get("filter", "all")
    category = category or request.GET.get("category")

    products = Product.objects.all()
    if filter_type == "my":
        products = products.filter(user=request.user)

    # <= ini penting!
    if category in dict(Product.CATEGORY_CHOICES):
        products = products.filter(category=category)

    context = {
        "npm": "2406399655",
        "name": request.user.username,
        "class": "PBP C",
        "products": products,
        "last_login": request.COOKIES.get("last_login", "Never"),
        "filter_type": filter_type,
        "active_category": category,   # dipakai untuk highlight navbar
    }
    return render(request, "home.html", context)

@login_required(login_url='/login')
def create_product(request):
    form = ProductForm(request.POST or None)
    if form.is_valid() and request.method == "POST":
        product_entry = form.save(commit=False)   
        product_entry.user = request.user         
        product_entry.save()
        return redirect('main:show_main')
    context = {'form': form}
    return render(request, "create_product.html", context)

@login_required(login_url='/login')
def show_product(request, id):
    product = get_object_or_404(Product, pk=id)
    context = {'product': product}
    return render(request, "show_product.html", context)

# Data Delivery Views
def show_xml(request):
    products = Product.objects.all()
    xml_data = serializers.serialize("xml", products)
    return HttpResponse(xml_data, content_type="application/xml")

def show_json(request):
    products = Product.objects.all()
    json_data = serializers.serialize("json", products)
    return HttpResponse(json_data, content_type="application/json")

def show_xml_by_id(request, product_id):
    try:
        product = Product.objects.filter(pk=product_id)
        xml_data = serializers.serialize("xml", product)
        return HttpResponse(xml_data, content_type="application/xml")
    except Product.DoesNotExist:
        return HttpResponse(status=404)

def show_json_by_id(request, product_id):
    try:
        product = Product.objects.get(pk=product_id)
        json_data = serializers.serialize("json", [product])
        return HttpResponse(json_data, content_type="application/json")
    except Product.DoesNotExist:
        return HttpResponse(status=404)
    
def register(request):
    form = UserCreationForm()

    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Your account has been successfully created!')
            return redirect('main:login')
    context = {'form':form}
    return render(request, 'register.html', context)

def login_user(request):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)

        if form.is_valid():
            user = form.get_user()
            login(request, user)
            response = HttpResponseRedirect(reverse("main:show_main"))
            response.set_cookie('last_login', str(datetime.datetime.now()))
            return response

    else:
        form = AuthenticationForm(request)
    context = {'form': form}
    return render(request, 'login.html', context)

def logout_user(request):
    logout(request)
    response = HttpResponseRedirect(reverse('main:login'))
    response.delete_cookie('last_login')
    return response

@login_required(login_url='/login')
def edit_product(request, id):
    product = get_object_or_404(Product, pk=id, user=request.user)  
    form = ProductForm(request.POST or None, instance=product)

    if form.is_valid() and request.method == "POST":
        form.save()
        return redirect('main:show_main')

    context = {'form': form, 'product': product}
    return render(request, "edit_product.html", context)

@login_required(login_url='/login')
def delete_product(request, id):
    product = get_object_or_404(Product, pk=id, user=request.user)  
    product.delete()
    return HttpResponseRedirect(reverse('main:show_main'))


def product_to_dict(p: Product):
    d = model_to_dict(p, fields=['id','name','price','stock','description','image_url','category'])
    d['created_at'] = p.created_at.isoformat() if p.created_at else None
    d['user_id'] = p.user_id
    d['user_username'] = p.user.username if p.user_id else None
    return d

@login_required(login_url='/login')
@require_http_methods(["GET"])
def api_products_list(request):
    """
    Query params:
      - filter=all|my  (default: all)
      - category=apparel|accessories|shoes (opsional)
    """
    flt = request.GET.get('filter', 'all')
    cat = request.GET.get('category')
    qs = Product.objects.all().order_by('-created_at')
    if flt == 'my':
        qs = qs.filter(user=request.user)
    if cat in dict(Product.CATEGORY_CHOICES):
        qs = qs.filter(category=cat)
    data = [product_to_dict(p) for p in qs]
    return JsonResponse({"results": data}, status=200)

@login_required(login_url='/login')
@require_http_methods(["GET"])
def api_product_detail(request, id):
    p = get_object_or_404(Product, pk=id)
    return JsonResponse(product_to_dict(p), status=200)

@login_required(login_url='/login')
@require_http_methods(["POST"])
def api_product_create(request):
    form = ProductForm(request.POST)
    if form.is_valid():
        obj = form.save(commit=False)
        obj.user = request.user
        obj.save()
        return JsonResponse({"message":"CREATED","product":product_to_dict(obj)}, status=201)
    return JsonResponse({"message":"VALIDATION_ERROR","errors":form.errors}, status=400)

@login_required(login_url='/login')
@require_http_methods(["POST","PUT","PATCH"])
def api_product_update(request, id):
    obj = get_object_or_404(Product, pk=id, user=request.user)
    data = request.POST or request.PUT if hasattr(request, "PUT") else request.POST
    form = ProductForm(data, instance=obj)
    if form.is_valid():
        form.save()
        return JsonResponse({"message":"UPDATED","product":product_to_dict(obj)}, status=200)
    return JsonResponse({"message":"VALIDATION_ERROR","errors":form.errors}, status=400)

@login_required(login_url='/login')
@require_http_methods(["POST","DELETE"])
def api_product_delete(request, id):
    obj = get_object_or_404(Product, pk=id, user=request.user)
    obj.delete()
    return JsonResponse({"message":"DELETED"}, status=200)

# -------- AUTH via AJAX --------

@require_http_methods(["GET"])
def api_get_csrf(request):
    # opsional jika ingin fetch CSRF via JS
    return JsonResponse({"csrftoken": get_token(request)})

@require_http_methods(["POST"])
def api_register(request):
    # Mengembalikan JSON (bukan redirect)
    form = UserCreationForm(request.POST or None)
    if form.is_valid():
        user = form.save()
        return JsonResponse({"message":"REGISTERED","username":user.username}, status=201)
    return JsonResponse({"message":"VALIDATION_ERROR","errors":form.errors}, status=400)

@require_http_methods(["POST"])
def api_login(request):
    username = request.POST.get('username')
    password = request.POST.get('password')
    user = authenticate(request, username=username, password=password)
    if user is not None:
        login(request, user)
        response = JsonResponse({"message":"LOGGED_IN","username":user.username}, status=200)
        response.set_cookie('last_login', str(datetime.datetime.now()))
        return response
    return JsonResponse({"message":"INVALID_CREDENTIALS"}, status=401)

@login_required(login_url='/login')
@require_http_methods(["POST"])
def api_logout(request):
    logout(request)
    response = JsonResponse({"message":"LOGGED_OUT"}, status=200)
    response.delete_cookie('last_login')
    return response