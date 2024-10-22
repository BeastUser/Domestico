# Generated by Django 5.1.1 on 2024-10-03 18:46

import datetime
import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Empdetails',
            fields=[
                ('sno', models.AutoField(primary_key=True, serialize=False)),
                ('username', models.CharField(default='EMP_', max_length=30)),
                ('fname', models.CharField(max_length=20)),
                ('lname', models.CharField(max_length=20)),
                ('phone', models.CharField(max_length=50)),
                ('email', models.CharField(max_length=30)),
                ('address', models.CharField(max_length=50)),
                ('work', models.CharField(max_length=30)),
                ('password', models.CharField(max_length=25)),
                ('dob', models.DateField(verbose_name=datetime.datetime)),
            ],
        ),
        migrations.CreateModel(
            name='Signup',
            fields=[
                ('sno', models.AutoField(primary_key=True, serialize=False)),
                ('username', models.CharField(max_length=30)),
                ('fname', models.CharField(max_length=20)),
                ('lname', models.CharField(max_length=20)),
                ('phone', models.CharField(max_length=50)),
                ('address', models.CharField(max_length=50)),
                ('city', models.CharField(default='Ahmedabad', max_length=50)),
                ('email', models.CharField(max_length=30)),
                ('password', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='Bookings',
            fields=[
                ('BookingId', models.AutoField(primary_key=True, serialize=False)),
                ('Employee', models.CharField(max_length=100)),
                ('category', models.CharField(max_length=500)),
                ('sno', models.CharField(max_length=50)),
                ('price', models.IntegerField()),
                ('booking_date', models.DateField(default=datetime.datetime.today)),
                ('service_date', models.DateField()),
                ('slote', models.CharField(max_length=20)),
                ('name', models.CharField(blank=True, max_length=30, null=True)),
                ('address', models.CharField(blank=True, max_length=200, null=True)),
                ('phone', models.BigIntegerField(default=0)),
                ('complete_status', models.BooleanField(default=False)),
                ('cancel_booking', models.BooleanField(default=False)),
                ('otp', models.IntegerField(default=0)),
                ('User', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]