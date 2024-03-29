# Generated by Django 4.0.4 on 2022-06-30 05:13

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='booking',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('number_of_persn', models.IntegerField()),
                ('adults', models.IntegerField()),
                ('childrens', models.IntegerField()),
                ('date_arrival', models.DateTimeField()),
                ('date_vaccate', models.DateTimeField()),
                ('status', models.CharField(max_length=50)),
                ('booking_date', models.DateTimeField()),
            ],
        ),
        migrations.CreateModel(
            name='cottage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cottage_num', models.IntegerField()),
                ('cottage_details', models.TextField()),
                ('number_rooms', models.IntegerField()),
                ('cottage_facility', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='employee',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('firstname', models.CharField(max_length=50)),
                ('lastname', models.CharField(max_length=50)),
                ('place', models.CharField(max_length=50)),
                ('street', models.CharField(max_length=50)),
                ('city', models.CharField(max_length=50)),
                ('pincode', models.IntegerField()),
                ('state', models.CharField(max_length=50)),
                ('district', models.CharField(max_length=50)),
                ('phone', models.BigIntegerField()),
                ('gender', models.CharField(max_length=50)),
                ('dob', models.DateField(max_length=50)),
                ('adarnumber', models.BigIntegerField()),
                ('salary', models.BigIntegerField()),
                ('emptype', models.CharField(max_length=50)),
                ('jobtitle', models.CharField(max_length=50)),
                ('photo', models.FileField(upload_to='')),
            ],
        ),
        migrations.CreateModel(
            name='events',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('event_name', models.CharField(max_length=50)),
                ('eve_desc', models.TextField()),
                ('rate', models.BigIntegerField()),
                ('photo', models.FileField(upload_to='')),
            ],
        ),
        migrations.CreateModel(
            name='facilities',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('faci_name', models.CharField(max_length=50)),
                ('rate', models.BigIntegerField()),
                ('desc', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='login',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=100)),
                ('password', models.CharField(max_length=50)),
                ('type', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='package',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pack_name', models.CharField(max_length=50)),
                ('rate', models.BigIntegerField()),
                ('photo', models.FileField(upload_to='')),
                ('description', models.TextField()),
                ('start_date', models.DateTimeField()),
                ('end_date', models.DateTimeField()),
            ],
        ),
        migrations.CreateModel(
            name='salary_info',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('salary_amount', models.BigIntegerField()),
                ('date', models.DateTimeField()),
                ('status', models.CharField(max_length=50)),
                ('emp_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='resortapp.employee')),
            ],
        ),
        migrations.CreateModel(
            name='room',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('room_number', models.CharField(max_length=50)),
                ('room_facility', models.CharField(max_length=50)),
                ('number_of_persons', models.IntegerField()),
                ('description', models.TextField()),
                ('photo', models.FileField(upload_to='')),
                ('rate', models.BigIntegerField()),
                ('cottage_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='resortapp.cottage')),
            ],
        ),
        migrations.CreateModel(
            name='request_materials',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('material_det', models.CharField(max_length=100)),
                ('quantity', models.BigIntegerField()),
                ('status', models.CharField(max_length=50)),
                ('emp_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='resortapp.employee')),
            ],
        ),
        migrations.CreateModel(
            name='registration',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('firstname', models.CharField(max_length=50)),
                ('lastname', models.CharField(max_length=50)),
                ('place', models.CharField(max_length=50)),
                ('street', models.CharField(max_length=50)),
                ('city', models.CharField(max_length=50)),
                ('pincode', models.IntegerField()),
                ('state', models.CharField(max_length=50)),
                ('country', models.CharField(max_length=50)),
                ('gender', models.CharField(max_length=50)),
                ('phone', models.BigIntegerField()),
                ('idproof', models.FileField(upload_to='')),
                ('email', models.CharField(max_length=50)),
                ('nationality', models.CharField(max_length=50)),
                ('loginid', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='resortapp.login')),
            ],
        ),

        migrations.CreateModel(
            name='offers',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('number_of_persn', models.IntegerField()),
                ('rate', models.FloatField()),
                ('start_date', models.DateField()),
                ('end_date', models.DateField()),
                ('offer_price', models.FloatField()),
                ('package_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='resortapp.package')),
            ],
        ),
        migrations.CreateModel(
            name='menu',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('item_name', models.CharField(max_length=50)),
                ('item_description', models.TextField()),
                ('rate', models.BigIntegerField()),
                ('stock', models.BigIntegerField()),
                ('cottage_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='resortapp.cottage')),
            ],
        ),
        migrations.CreateModel(
            name='leave',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField()),
                ('status', models.CharField(max_length=50)),
                ('reason', models.TextField()),
                ('requestdate', models.DateField()),
                ('employeeid', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='resortapp.employee')),
            ],
        ),
        migrations.CreateModel(
            name='feedback',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.TextField()),
                ('rating', models.FloatField()),
                ('date', models.DateField()),
                ('user_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='resortapp.registration')),
            ],
        ),
        migrations.CreateModel(
            name='event_book',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status', models.CharField(max_length=50)),
                ('requirements', models.TextField(max_length=100)),
                ('booking_date', models.DateField()),
                ('event_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='resortapp.events')),
                ('user_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='resortapp.registration')),
            ],
        ),
        migrations.AddField(
            model_name='employee',
            name='loginid',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='resortapp.login'),
        ),
        migrations.CreateModel(
            name='chat',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('message', models.TextField()),
                ('date_time', models.DateTimeField()),
                ('emp_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='emp_id', to='resortapp.login')),
                ('user_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='user_id', to='resortapp.login')),
            ],
        ),
        migrations.AddField(
            model_name='booking',
            name='facilities_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='resortapp.facilities'),
        ),
        migrations.AddField(
            model_name='booking',
            name='package_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='resortapp.package'),
        ),
        migrations.AddField(
            model_name='booking',
            name='room_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='resortapp.room'),
        ),
        migrations.AddField(
            model_name='booking',
            name='user_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='resortapp.registration'),
        ),
    ]
