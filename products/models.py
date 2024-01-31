from django.db import models

class Category(models.Model):
    category = models.CharField(max_length=254)
    product_type_name = models.CharField(max_length=254, null=True, blank=True)

    def __str__(self):
        return self.product_type_name
    
    def get_product_type(self):
        return self.product_type

class Product(models.Model):
    category = models.ForeignKey('Category', null=True, blank=True, on_delete=models.SET_NULL)
    product_name = models.CharField(max_length=254)
    product_img = models.ImageField(null=True, blank=True)
    ingredients = models.TextField()
    price = models.DecimalField(max_digits=6, decimal_places=2)

    def __str__(self):
        return self.product_name
