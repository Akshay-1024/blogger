# Generated by Django 3.2.4 on 2021-06-26 03:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_blogpost_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blogpost',
            name='image',
            field=models.ImageField(default='default.jpg', upload_to='blog_images'),
        ),
    ]
