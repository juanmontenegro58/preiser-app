# Generated by Django 2.0.6 on 2018-12-11 16:42

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Aprendiz',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=100)),
                ('apellido', models.CharField(max_length=100)),
                ('identificacion', models.IntegerField(unique=True)),
                ('tipo_documento', models.CharField(max_length=50)),
                ('estado', models.BooleanField(default=True)),
            ],
        ),
        migrations.CreateModel(
            name='Bodega',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=100, unique=True)),
                ('foto', models.ImageField(blank=True, null=True, upload_to='fotos')),
            ],
        ),
        migrations.CreateModel(
            name='Bodega_Material',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fecha_ingresa', models.DateField(default='2018-12-11')),
                ('fecha_salida', models.DateField(blank=True, null=True)),
                ('bodega', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='home.Bodega')),
            ],
        ),
        migrations.CreateModel(
            name='Categoria',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=100, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Cuentadante',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=100)),
                ('identificacion', models.IntegerField(unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Detalle_Prestamo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cantidad', models.IntegerField()),
                ('estado_elemento_prestamo', models.CharField(blank=True, max_length=50, null=True)),
                ('descripcion', models.TextField(blank=True, max_length=1000, null=True)),
                ('tipo_daño', models.CharField(blank=True, max_length=6, null=True)),
                ('estado_devolucion', models.CharField(blank=True, max_length=50, null=True)),
                ('fecha_devolucion', models.DateField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Ficha',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('numero_ficha', models.IntegerField(unique=True)),
                ('fecha_inicio', models.DateField()),
                ('fecha_finalizacion', models.DateField(blank=True, null=True)),
                ('estado', models.BooleanField(default=True)),
            ],
        ),
        migrations.CreateModel(
            name='Marca',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=100, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Material',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tipo_elemento', models.CharField(max_length=100)),
                ('codigo_sena', models.CharField(blank=True, max_length=100, null=True, unique=True)),
                ('numero_serie', models.CharField(blank=True, max_length=100, null=True, unique=True)),
                ('cantidad', models.IntegerField(blank=True, default=1)),
                ('estado', models.CharField(choices=[('Disponible', 'Disponible'), ('No Disponible', 'No Disponible')], default='Disponible', max_length=100)),
                ('imagen', models.ImageField(blank=True, null=True, upload_to='fotos')),
                ('categoria', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='home.Categoria')),
                ('cuentadante', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='home.Cuentadante')),
                ('ficha', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='home.Ficha')),
                ('marca', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='home.Marca')),
            ],
        ),
        migrations.CreateModel(
            name='Nombre_Material',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=100, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Prestamo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fecha_prestamo', models.DateField(default='2018-12-11')),
                ('estado', models.CharField(default='Activo', max_length=50)),
                ('fecha_entrega', models.DateField()),
                ('aprendiz', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='home.Aprendiz')),
            ],
        ),
        migrations.CreateModel(
            name='Programa',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=100, unique=True)),
            ],
        ),
        migrations.AddField(
            model_name='material',
            name='nombre',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='home.Nombre_Material'),
        ),
        migrations.AddField(
            model_name='ficha',
            name='programa',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='home.Programa'),
        ),
        migrations.AddField(
            model_name='detalle_prestamo',
            name='material',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='home.Material'),
        ),
        migrations.AddField(
            model_name='detalle_prestamo',
            name='prestamo',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='detalles', to='home.Prestamo'),
        ),
        migrations.AddField(
            model_name='bodega_material',
            name='material',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='home.Material'),
        ),
        migrations.AddField(
            model_name='aprendiz',
            name='ficha',
            field=models.ManyToManyField(blank=True, null=True, to='home.Ficha'),
        ),
    ]
