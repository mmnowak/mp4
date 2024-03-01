from django.db import models
from django.contrib.auth.models import User
from products.models import Product

# Create your models here.

class Favourites(models.Model):
    """ Model for users' favourites lists """

    products = models.ManyToManyField(
        Product,
        blank=True
    )

    username = models.OneToOneField(
        User,
        on_delete=models.CASCADE
    )

    def __str__(self):
        return f"{self.username}'s Favourites"

