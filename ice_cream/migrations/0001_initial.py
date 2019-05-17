# Generated by Django 2.2.1 on 2019-05-15 19:26

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Menu',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('flavor', models.CharField(max_length=75)),
                ('date_churned', models.DateField()),
                ('available', models.CharField(choices=[('D', 'daily'), ('W', 'weekly'), ('S', 'seasonal')], max_length=75)),
                ('base', models.CharField(choices=[('C', 'chocolate'), ('V', 'vanilla')], max_length=75)),
            ],
        ),
    ]
