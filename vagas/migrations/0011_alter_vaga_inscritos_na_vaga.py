# Generated by Django 4.0.6 on 2022-08-07 13:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vagas', '0010_vaga_inscritos_na_vaga'),
    ]

    operations = [
        migrations.AlterField(
            model_name='vaga',
            name='inscritos_na_vaga',
            field=models.CharField(max_length=100),
        ),
    ]
