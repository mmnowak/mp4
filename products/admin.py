from django.contrib import admin
from .models import Product, Category

class ProductAdmin(admin.ModelAdmin):
    list_display = (
        'category',
        'product_name',
        'product_img',
        'ingredients',
        'price',
    )

    ordering = ('product_name',)

class CategoryAdmin(admin.ModelAdmin):
    list_display = (
        'category',
        'product_type_name',
    )


# Register your models here.
admin.site.register(Product, ProductAdmin)
admin.site.register(Category, CategoryAdmin)
