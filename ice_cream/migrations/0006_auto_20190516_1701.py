# Generated by Django 2.2.1 on 2019-05-16 17:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ice_cream', '0005_auto_20190516_1659'),
    ]

    operations = [
        migrations.AlterField(
            model_name='menu',
            name='featured',
            field=models.BooleanField(),
        ),
    ]