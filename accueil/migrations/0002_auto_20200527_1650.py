# Generated by Django 2.0 on 2020-05-27 14:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accueil', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='accueil',
            options={'verbose_name': 'Parcours', 'verbose_name_plural': 'Parcours'},
        ),
        migrations.AddField(
            model_name='accueil',
            name='qr_code',
            field=models.ImageField(blank=True, upload_to=''),
        ),
        migrations.AlterField(
            model_name='accueil',
            name='description',
            field=models.TextField(verbose_name='Description générale'),
        ),
        migrations.AlterField(
            model_name='accueil',
            name='image',
            field=models.ImageField(blank=True, upload_to=''),
        ),
        migrations.AlterField(
            model_name='accueil',
            name='resume',
            field=models.TextField(verbose_name='Petit résumé'),
        ),
        migrations.AlterField(
            model_name='accueil',
            name='title',
            field=models.CharField(default='', max_length=100, verbose_name='Nom du parcours'),
        ),
    ]
