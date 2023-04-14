# Generated by Django 4.2 on 2023-04-13 21:53

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Agente',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Nombre_Agente', models.CharField(max_length=200)),
                ('Email', models.CharField(max_length=50)),
                ('Password', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Asegurado',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Nombre_Asegurado', models.CharField(max_length=200)),
                ('Edad', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Cliente',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Nombre_Cliente', models.CharField(max_length=200)),
                ('Telefono', models.CharField(max_length=10)),
                ('Email', models.CharField(max_length=50)),
                ('Id_Agente', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.agente')),
            ],
        ),
        migrations.CreateModel(
            name='Estado_Poliza',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Estado_Poliza', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Tipo_Poliza',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Tipo_Poliza', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Poliza',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Num_Poliza', models.IntegerField()),
                ('Fecha_Inicio', models.DateField()),
                ('Fecha_Vigencia', models.DateField()),
                ('Aseguradora', models.CharField(max_length=200)),
                ('Precio', models.FloatField()),
                ('Estado_Poliza', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.estado_poliza')),
                ('Id_Asegurado', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.asegurado')),
                ('Id_Cliente', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.cliente')),
                ('Tipo_Poliza', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.tipo_poliza')),
            ],
        ),
    ]
