# from django.forms import ModelForm
# from main.models import Product

# class ProductForm(ModelForm):
#     class Meta:
#         model = Product
#         fields = ["name", "price", "stock", "description", "image_url", "category"]

# forms.py
from django.forms import ModelForm
from django.utils.html import strip_tags
from main.models import Product

class ProductForm(ModelForm):
    class Meta:
        model = Product
        fields = ["name", "price", "stock", "description", "image_url", "category"]

    def clean_name(self):
        return strip_tags(self.cleaned_data["name"])

    def clean_description(self):
        return strip_tags(self.cleaned_data["description"])
