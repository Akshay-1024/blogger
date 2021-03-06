# Generated by Django 3.2.4 on 2021-06-26 15:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='bio',
            field=models.TextField(default='', max_length=80),
        ),
        migrations.AddField(
            model_name='profile',
            name='website',
            field=models.TextField(default=''),
        ),
        migrations.AlterField(
            model_name='profile',
            name='image',
            field=models.ImageField(default='default_profile_pic.jpeg', upload_to='profile_pics'),
        ),
    ]
