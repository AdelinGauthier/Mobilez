# Generated by Django 3.0.5 on 2020-08-15 22:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accueil', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='GalleryPhotos',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=254)),
                ('images', models.ImageField(upload_to='images/')),
            ],
        ),
    ]