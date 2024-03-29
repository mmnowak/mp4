from django import forms
from .widgets import CustomClearableFileInput
from .models import Product, Category


class ProductForm(forms.ModelForm):

    class Meta:
        model = Product
        fields = '__all__'

        labels = {
            'category': 'Product Category',
            'product_name': 'Product Name',
            'ingredients': 'Product Ingredients',
            'product_img': 'Image',
            'price': 'Price',
            'rating': 'Rating',
        }

    product_img = forms.ImageField(label='Image',
                                   required=True,
                                   widget=CustomClearableFileInput)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        categories = Category.objects.all()

        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'border-black rounded-0'
