# Generated by Django 2.2.1 on 2019-05-17 16:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ice_cream', '0013_auto_20190516_1803'),
    ]

    operations = [
        migrations.AddField(
            model_name='menu',
            name='model_pic',
            field=models.ImageField(default='pic_folder/None/no-img.jpg', upload_to='pic_folder/'),
        ),
    ]
