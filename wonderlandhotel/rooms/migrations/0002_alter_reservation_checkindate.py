# Generated by Django 3.2 on 2021-04-24 22:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rooms', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='reservation',
            name='checkinDate',
            field=models.DateField(auto_now_add=True),
        ),
    ]
