# Generated by Django 3.2.9 on 2021-11-19 11:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('my_shop', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='stars',
            field=models.FloatField(verbose_name='Рейтинг'),
        ),
    ]
