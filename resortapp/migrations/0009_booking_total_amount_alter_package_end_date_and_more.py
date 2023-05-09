# Generated by Django 4.0.4 on 2022-07-18 05:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('resortapp', '0008_leave_todate'),
    ]

    operations = [
        migrations.AddField(
            model_name='booking',
            name='total_amount',
            field=models.FloatField(default=12333),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='package',
            name='end_date',
            field=models.DateField(),
        ),
        migrations.AlterField(
            model_name='package',
            name='start_date',
            field=models.DateField(),
        ),
    ]