from django.db import models
from django.core.validators import (
    MaxValueValidator, MinValueValidator
)

from products.models import Product
from django.contrib.auth.models import User

# Create your models here.


class Review(models.Model):
    """ Model for a Review form """
    product = models.ForeignKey(Product, null=True, blank=True,
                                on_delete=models.CASCADE)
    user = models.ForeignKey(User, null=True, blank=True,
                             on_delete=models.CASCADE)
    date = models.DateField(auto_now_add=True, blank=False, null=False)
    title = models.CharField(max_length=50)
    content = models.TextField(max_length=500)
    rating = models.IntegerField(
        validators=[
            MaxValueValidator(5),
            MinValueValidator(1)
        ],
        default=0,
        blank=False,
        null=False
    )

    def __str__(self):
        """ String representation of Review title """
        return self.title
