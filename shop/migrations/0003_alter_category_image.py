# Generated by Django 5.1.2 on 2025-01-16 18:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0002_category_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='image',
            field=models.ImageField(upload_to='category_images/'),
        ),
    ]
