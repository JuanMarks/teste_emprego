# Generated by Django 4.0.6 on 2022-07-31 20:40

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Vaga',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome_vaga', models.CharField(max_length=70)),
                ('faixa_salarial', models.IntegerField()),
                ('escolaridade', models.CharField(choices=[('Ensino Fundamental', 'Ensino Fundamental'), ('Ensino Medio', 'Ensino Medio'), ('Tecnologo', 'Tecnologo'), ('Ensino Superior', 'Ensino Superior'), ('Pos', 'Pos'), ('MBA', 'MBA'), ('Mestrado', 'Mestrado'), ('Doutorado', 'Doutorado')], max_length=400)),
            ],
        ),
    ]
