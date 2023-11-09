from django.db import models
from django.utils import timezone

# Create your models here.

class ProductClass(models.Model):
    name = models.CharField(max_length=100)
    created_at = models.DateField(default=timezone.now)

    def __str__(self) -> str:
        return self.name


class Category(models.Model):
    name = models.CharField(max_length=100)
    product_class = models.ForeignKey(ProductClass, on_delete=models.CASCADE)

    def __str__(self) -> str:
        return self.name

class Subcategory(models.Model):
    type = models.IntegerField()
    category = models.ForeignKey(Category, on_delete=models.CASCADE)



class Material(models.Model):
    material = models.CharField(max_length=255)
    created_at = models.DateField(default=timezone.now)

    def __str__(self) -> str:
        return self.material


class Color(models.Model):
    color = models.CharField(max_length=255)
    created_at = models.DateField(default=timezone.now)

    def __str__(self) -> str:
        return self.color


class Product(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    height = models.DecimalField(max_digits=5, decimal_places=2, blank=True)
    length = models.DecimalField(max_digits=5, decimal_places=2, blank=True)
    depth = models.DecimalField(max_digits=5, decimal_places=2, blank=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    discount = models.DecimalField(max_digits=5, decimal_places=2, blank=True)
    created_at = models.DateTimeField(default=timezone.now)
    photo = models.ImageField(upload_to='product/images/')

    product_class = models.ForeignKey(ProductClass, null=True, on_delete=models.CASCADE)
    category = models.ForeignKey(Category, null=True, on_delete=models.CASCADE)
    subcategory = models.ForeignKey(Subcategory, null=True, on_delete=models.CASCADE)

    material = models.ManyToManyField(Material)
    color = models.ManyToManyField(Color)

    def __str__(self) -> str:
        return self.name
