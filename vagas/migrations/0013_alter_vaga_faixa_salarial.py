# Generated by Django 4.0.6 on 2022-08-08 12:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vagas', '0012_alter_vaga_faixa_salarial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='vaga',
            name='faixa_salarial',
            field=models.CharField(choices=[('Até 1000', 'Até 1000'), ('de 1000 a 2000', 'de 1000 a 2000'), ('de 2000 a 3000', 'de 2000 a 3000'), ('Acima de 3000', 'Acima de 3000')], max_length=50),
        ),
    ]
