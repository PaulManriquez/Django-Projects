# Generated by Django 5.0.7 on 2024-07-17 00:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ordersManage', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customer',
            name='Email',
            field=models.EmailField(blank=True, max_length=254, null=True),
        ),
    ]
