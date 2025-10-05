from django.urls import path
from main.views import show_main, create_product, show_product, show_xml, show_json, show_xml_by_id, show_json_by_id, register, login_user, logout_user, edit_product, delete_product, api_products_list, api_product_detail, api_product_create, api_product_update, api_product_delete, api_login, api_register, api_logout

app_name = 'main'

urlpatterns = [
    path('', show_main, name='show_main'),

      # kategori (pakai show_main dengan default kwargs)
    path('apparel/', show_main, {'category': 'apparel'}, name='apparel'),
    path('accessories/', show_main, {'category': 'accessories'}, name='accessories'),
    path('shoes/', show_main, {'category': 'shoes'}, name='shoes'),
    
    path('create-product/', create_product, name='create_product'),
    path('product/<int:id>/', show_product, name='show_product'),
    path('xml/', show_xml, name='show_xml'),
    path('json/', show_json, name='show_json'),
    path('xml/<int:product_id>/', show_xml_by_id, name='show_xml_by_id'),
    path('json/<int:product_id>/', show_json_by_id, name='show_json_by_id'),
    path('register/', register, name='register'),
    path('login/', login_user, name='login'),
    path('logout/', logout_user, name='logout'),
    path('product/<int:id>/edit/', edit_product, name='edit_product'),
    path('product/<int:id>/delete/', delete_product, name='delete_product'),

    path('api/products/', api_products_list, name='api_products_list'),
    path('api/products/<int:id>/', api_product_detail, name='api_product_detail'),
    path('api/products/create/', api_product_create, name='api_product_create'),
    path('api/products/<int:id>/update/', api_product_update, name='api_product_update'),
    path('api/products/<int:id>/delete/', api_product_delete, name='api_product_delete'),

    # Auth via AJAX
    path('api/auth/login/', api_login, name='api_login'),
    path('api/auth/register/', api_register, name='api_register'),
    path('api/auth/logout/', api_logout, name='api_logout'),
]
