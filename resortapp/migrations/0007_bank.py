# Generated by Django 4.0.4 on 2022-07-14 10:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('resortapp', '0006_menu_order_details_menu_orders_delete_menubooking_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='bank',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('bank_name', models.CharField(max_length=50)),
                ('ifsc', models.CharField(max_length=50)),
                ('pin', models.BigIntegerField()),
                ('account_no', models.BigIntegerField()),
                ('amount', models.FloatField()),
            ],
        ),
    ]
