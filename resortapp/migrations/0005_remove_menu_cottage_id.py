# Generated by Django 4.0.4 on 2022-07-14 03:42

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('resortapp', '0004_menu_photo_menubooking'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='menu',
            name='cottage_id',
        ),
    ]
