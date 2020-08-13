

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Accueil',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(default='', max_length=100, verbose_name='Nom du parcours')),
                ('resume', models.TextField(verbose_name='Petit résumé')),
                ('description', models.TextField(verbose_name='Description générale')),
                ('map_url_data', models.TextField(validators=[django.core.validators.URLValidator()])),
                ('image', models.ImageField(blank=True, upload_to='')),
                ('qr_code', models.ImageField(blank=True, upload_to='')),
            ],
            options={
                'verbose_name': 'Parcours',
                'verbose_name_plural': 'Parcours',
            },
        ),
    ]
