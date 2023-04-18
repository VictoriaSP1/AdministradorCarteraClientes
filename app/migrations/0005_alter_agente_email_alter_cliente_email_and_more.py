# Generated by Django 4.2 on 2023-04-18 00:09

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0004_aseguradora_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='agente',
            name='Email',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='cliente',
            name='Email',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='poliza',
            name='Id_Asegurado',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.asegurado'),
        ),
        migrations.DeleteModel(
            name='Poliza_Asegurado',
        ),
    ]