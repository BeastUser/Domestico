# Generated by Django 5.1.1 on 2024-10-03 18:39

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Services', '0018_alter_review_dt'),
    ]

    operations = [
        migrations.AlterField(
            model_name='review',
            name='dt',
            field=models.DateField(default=datetime.date(2024, 10, 4)),
        ),
    ]
