# Generated by Django 2.2.1 on 2019-05-16 17:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ice_cream', '0007_remove_menu_featured'),
    ]

    operations = [
        migrations.AddField(
            model_name='menu',
            name='featured',
            field=models.BooleanField(default=True),
        ),
    ]
