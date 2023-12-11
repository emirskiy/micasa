from django.contrib import admin
from .models import Product, Material, Color, Category, Subcategory
# Register your models here.

admin.site.register(Product)
admin.site.register(Material)
admin.site.register(Color)
admin.site.register(Category)
admin.site.register(Subcategory)