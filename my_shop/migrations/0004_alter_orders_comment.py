# Generated by Django 3.2.9 on 2021-11-26 11:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('my_shop', '0003_alter_orders_country'),
    ]

    operations = [
        migrations.AlterField(
            model_name='orders',
            name='comment',
            field=models.TextField(blank=True, verbose_name='Коментарий'),
        ),
    ]