# Generated by Django 2.2.4 on 2019-08-28 00:43

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Articulo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('autor', models.CharField(max_length=50)),
                ('titulo', models.CharField(max_length=120)),
                ('descripcion', models.CharField(max_length=200)),
                ('cuerpo', models.TextField()),
                ('ubicacion', models.CharField(max_length=120)),
                ('fecha_publicacion', models.DateField()),
                ('activo', models.BooleanField(default=True)),
                ('fecha_creado', models.DateField(auto_now_add=True)),
                ('fecha_actualizado', models.DateTimeField(auto_now=True)),
            ],
        ),
    ]
