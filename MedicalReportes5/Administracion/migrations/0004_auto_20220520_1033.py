# Generated by Django 3.2 on 2022-05-20 15:33

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Administracion', '0003_alter_mae_reportes_mae_subgruporeportes'),
    ]

    operations = [
        migrations.RenameField(
            model_name='mae_subgruporeportes',
            old_name='mae_subgruporeportes',
            new_name='mae_gruporeportes',
        ),
        migrations.AlterField(
            model_name='mae_reportes',
            name='mae_subgruporeportes',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.PROTECT, to='Administracion.mae_subgruporeportes'),
        ),
    ]
