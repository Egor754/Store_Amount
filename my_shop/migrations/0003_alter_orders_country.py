# Generated by Django 3.2.9 on 2021-11-26 11:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('my_shop', '0002_alter_orders_comment'),
    ]

    operations = [
        migrations.AlterField(
            model_name='orders',
            name='country',
            field=models.CharField(choices=[('USA', 'United States'), ('UK', 'United Kingdom'), ('GERM', 'Germany'), ('FR', 'France'), ('IND', 'India'), ('AUST', 'Australia'), ('BR', 'Brazil'), ('CAN', 'Canada')], max_length=255, verbose_name='Страна'),
        ),
    ]
