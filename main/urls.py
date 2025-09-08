from django.urls import path # type: ignore
from . import views

urlpatterns = [
    path('', views.show_home, name='show_home'),
]
