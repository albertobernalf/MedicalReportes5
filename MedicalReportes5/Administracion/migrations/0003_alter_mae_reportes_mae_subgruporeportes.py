# Generated by Django 3.2 on 2022-05-20 15:29

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Administracion', '0002_auto_20220520_1022'),
    ]

    operations = [
        migrations.AlterField(
            model_name='mae_reportes',
            name='mae_subgruporeportes',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='Administracion.mae_subgruporeportes'),
        ),
    ]
