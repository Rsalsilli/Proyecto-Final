# Generated by Django 4.0.6 on 2022-07-20 22:26

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Categorias',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombreCat', models.CharField(max_length=30)),
                ('imagenCat', models.ImageField(upload_to='')),
            ],
        ),
        migrations.CreateModel(
            name='Streamers',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=30)),
                ('followers', models.IntegerField()),
                ('imagen', models.ImageField(upload_to='')),
                ('canalLink', models.CharField(max_length=100)),
                ('categorias', models.CharField(max_length=30)),
                ('peakViewers', models.IntegerField()),
                ('followerChange', models.IntegerField()),
                ('hoursViewers', models.IntegerField()),
            ],
        ),
    ]
