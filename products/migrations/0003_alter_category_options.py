# Generated by Django 3.2.23 on 2024-02-14 18:57

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0002_rename_product_type_category_category'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='category',
            options={'verbose_name_plural': 'Categories'},
        ),
    ]