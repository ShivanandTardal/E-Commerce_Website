# Generated by Django 4.1.7 on 2023-03-27 14:49

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0002_product_image'),
    ]

    operations = [
        migrations.RenameField(
            model_name='product',
            old_name='disital',
            new_name='digital',
        ),
    ]
