# Generated by Django 4.2 on 2023-04-11 09:41

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Services', '0013_alter_review_dt'),
    ]

    operations = [
        migrations.AlterField(
            model_name='review',
            name='dt',
            field=models.DateField(default=datetime.date(2023, 4, 11)),
        ),
    ]
