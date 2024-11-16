# Generated by Django 5.1.3 on 2024-11-15 21:14

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Libro',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titulo', models.CharField(max_length=200)),
                ('autor', models.CharField(max_length=100)),
                ('fecha_publicacion', models.DateField()),
                ('isbn', models.CharField(max_length=14)),
            ],
        ),
    ]
