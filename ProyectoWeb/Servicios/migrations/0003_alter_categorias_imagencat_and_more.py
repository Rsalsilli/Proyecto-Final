# Generated by Django 4.0.6 on 2022-07-24 21:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Servicios', '0002_alter_streamers_imagen'),
    ]

    operations = [
        migrations.AlterField(
            model_name='categorias',
            name='imagenCat',
            field=models.ImageField(upload_to='categoria'),
        ),
        migrations.RemoveField(
            model_name='streamers',
            name='categorias',
        ),
        migrations.AddField(
            model_name='streamers',
            name='categorias',
            field=models.ManyToManyField(to='Servicios.categorias'),
        ),
    ]
