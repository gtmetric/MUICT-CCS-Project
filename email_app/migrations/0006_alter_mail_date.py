# Generated by Django 3.2 on 2021-05-04 07:36

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('email_app', '0005_auto_20210503_1811'),
    ]

    operations = [
        migrations.AlterField(
            model_name='mail',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2021, 5, 4, 7, 36, 58, 881658, tzinfo=utc)),
        ),
    ]
