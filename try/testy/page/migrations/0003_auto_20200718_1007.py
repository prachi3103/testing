# Generated by Django 3.0.8 on 2020-07-18 04:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('page', '0002_auto_20200717_2353'),
    ]

    operations = [
        migrations.AlterField(
            model_name='page',
            name='image',
            field=models.ImageField(default='default.jpg', upload_to='profile_pics'),
        ),
    ]