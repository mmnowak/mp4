# Generated by Django 3.2.23 on 2024-01-31 22:37

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='category',
            old_name='product_type',
            new_name='category',
        ),
    ]
