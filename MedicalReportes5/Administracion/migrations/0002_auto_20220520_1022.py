# Generated by Django 3.2 on 2022-05-20 15:22

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Administracion', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Mae_SubGrupoReportes',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('nom_subgrupo', models.CharField(max_length=120, unique=True)),
                ('estadoreg', models.CharField(choices=[('A', 'Activo'), ('I', 'Inactivo')], default='A', max_length=1)),
                ('mae_subgruporeportes', models.ForeignKey(default=1, on_delete=django.db.models.deletion.PROTECT, to='Administracion.mae_gruporeportes')),
            ],
        ),
        migrations.AddField(
            model_name='mae_reportes',
            name='mae_subgruporeportes',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.PROTECT, to='Administracion.mae_subgruporeportes'),
        ),
    ]
