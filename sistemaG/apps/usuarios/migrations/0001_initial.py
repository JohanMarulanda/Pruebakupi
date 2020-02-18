# Generated by Django 2.2.6 on 2020-02-18 20:29

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ciudad',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('idCiudad', models.IntegerField(default=0)),
                ('nomCiudad', models.CharField(default='', max_length=255)),
                ('idDepartamento', models.IntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='cliente',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('cedula', models.IntegerField(default=0)),
                ('nombre', models.CharField(default='', max_length=255)),
                ('telefono', models.IntegerField(default=0)),
                ('correo', models.CharField(default='', max_length=255)),
                ('ciudad', models.CharField(default='', max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='departamento',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('idDepartamento', models.IntegerField(default=0)),
                ('nomDepartamento', models.CharField(default='', max_length=255)),
            ],
        ),
    ]
