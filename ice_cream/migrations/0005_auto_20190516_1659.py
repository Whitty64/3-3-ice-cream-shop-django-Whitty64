# Generated by Django 2.2.1 on 2019-05-16 16:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ice_cream', '0004_auto_20190516_1655'),
    ]

    operations = [
        migrations.AlterField(
            model_name='menu',
            name='featured',
            field=models.BooleanField(verbose_name=True),
        ),
    ]