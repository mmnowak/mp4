from django.contrib import admin
from .models import Review

class ReviewAdmin(admin.ModelAdmin):
    """
    Review Model Admin
    """

    list_display = (
        'product',
        'user',
        'date',
        'title',
        'rating',
        )

admin.site.register(Review, ReviewAdmin)