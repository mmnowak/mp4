from django.db import models
from django.core.validators import (
    MaxValueValidator, MinValueValidator
)

class Category(models.Model):

    class Meta:
        verbose_name_plural = 'Categories'
        
    category = models.CharField(max_length=254)
    product_type_name = models.CharField(max_length=254, null=True, blank=True)

    def __str__(self):
        return self.category
    
    def get_product_type(self):
        return self.product_type_name

class Product(models.Model):
    category = models.ForeignKey('Category', null=True, blank=True, on_delete=models.SET_NULL)
    product_name = models.CharField(max_length=254)
    product_img = models.ImageField()
    ingredients = models.TextField()
    price = models.DecimalField(max_digits=6, decimal_places=2)
    rating = models.IntegerField(
        default=0,
        null=True,
        blank=True,
        validators=[
            MaxValueValidator(5, message="Must be between 0-5"),
            MinValueValidator(0, message="Must be between 0-5")
        ],
    )

    def __str__(self):
        return self.product_name
    