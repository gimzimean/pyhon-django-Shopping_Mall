# Generated by Django 3.0.7 on 2020-06-17 07:06

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0002_auto_20200616_0810'),
    ]

    operations = [
        migrations.RenameField(
            model_name='product',
            old_name='stock',
            new_name='stuck',
        ),
    ]
