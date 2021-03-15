# Generated by Django 3.1.5 on 2021-03-09 04:52

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('ec', '0002_auto_20210304_1548'),
    ]

    operations = [
        migrations.CreateModel(
            name='PurchaseHistory',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_added', models.DateField(auto_now_add=True)),
                ('purchase_detail', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='ec.cartitem')),
            ],
        ),
    ]