# Generated by Django 4.0.6 on 2022-08-04 13:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('candidatos', '0002_candidato_pessoa'),
    ]

    operations = [
        migrations.AddField(
            model_name='candidato',
            name='email',
            field=models.EmailField(default='', max_length=254),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='candidato',
            name='nome_candidato',
            field=models.CharField(default='', max_length=30),
            preserve_default=False,
        ),
    ]
