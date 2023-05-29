# Generated by Django 4.2 on 2023-04-03 16:03

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Empresa',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Plan',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=100)),
                ('fecha', models.DateField()),
            ],
        ),
        migrations.CreateModel(
            name='TipoDeEquipo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Linea',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('numero_de_serie', models.CharField(max_length=100)),
                ('numero_de_telefono', models.CharField(max_length=100)),
                ('estado', models.CharField(choices=[('Activa', 'Activa'), ('Pendiente', 'Pendiente'), ('Baja', 'Baja')], max_length=20)),
                ('empresa', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='produccion.empresa')),
                ('plan', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='produccion.plan')),
            ],
        ),
        migrations.CreateModel(
            name='Equipo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('numero_de_serie', models.CharField(max_length=100)),
                ('imei', models.CharField(max_length=100)),
                ('estado', models.CharField(choices=[('Activo', 'Activo'), ('Inactivo', 'Inactivo'), ('Baja', 'Baja')], max_length=20)),
                ('linea', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='produccion.linea')),
                ('tipodeEquipo', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='produccion.tipodeequipo')),
            ],
        ),
    ]