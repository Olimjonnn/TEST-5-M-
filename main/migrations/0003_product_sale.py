# Generated by Django 3.2.9 on 2022-04-16 10:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_cart_info_wishlist'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='sale',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]