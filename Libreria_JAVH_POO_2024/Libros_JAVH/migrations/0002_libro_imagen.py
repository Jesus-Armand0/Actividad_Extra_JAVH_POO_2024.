# Generated by Django 5.1.3 on 2024-11-16 00:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Libros_JAVH', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='libro',
            name='imagen',
            field=models.ImageField(blank=True, null=True, upload_to='libros_imagenes/'),
        ),
    ]
