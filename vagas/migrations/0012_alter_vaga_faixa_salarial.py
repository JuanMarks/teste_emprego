# Generated by Django 4.0.6 on 2022-08-08 11:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vagas', '0011_alter_vaga_inscritos_na_vaga'),
    ]

    operations = [
        migrations.AlterField(
            model_name='vaga',
            name='faixa_salarial',
            field=models.CharField(max_length=50),
        ),
    ]
