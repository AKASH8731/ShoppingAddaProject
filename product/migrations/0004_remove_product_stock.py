# Generated by Django 4.2.1 on 2023-05-29 08:48

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0003_alter_product_slug_alter_producttag_slug'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='stock',
        ),
    ]