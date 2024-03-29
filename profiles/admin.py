from django.contrib import admin
from .models import UserProfile


class UserProfileAdmin(admin.ModelAdmin):
    """
    UserProfile Model Admin
    """

    fields = (
        'user', 'default_street_address1', 'default_street_address2',
        'default_town_or_city', 'default_postcode',
        'default_phone_number',)

    list_display = (
        'user', 'default_street_address1', 'default_street_address2',
        'default_town_or_city', 'default_postcode',
        'default_phone_number',)


admin.site.register(UserProfile, UserProfileAdmin)
