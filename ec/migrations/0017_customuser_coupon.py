# Generated by Django 3.1.5 on 2021-03-24 04:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ec', '0016_auto_20210318_1330'),
    ]

    operations = [
        migrations.AddField(
            model_name='customuser',
            name='coupon',
            field=models.IntegerField(null=True),
        ),
    ]