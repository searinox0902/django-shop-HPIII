# Generated by Django 4.0.4 on 2022-05-30 18:57

from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('tiposLicores', '0001_initial'),
        ('tiposDocumento', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Producto',
            fields=[
                ('idProduct', models.CharField(max_length=6, primary_key=True, serialize=False)),
                ('title', models.CharField(max_length=100)),
                ('description', models.TextField(max_length=300)),
                ('mark', models.CharField(max_length=30)),
                ('value', models.CharField(max_length=30)),
                ('dateCreation', models.DateField(auto_now=True, verbose_name='Fecha de Creacón')),
                ('image', models.CharField(max_length=100)),
                ('stock', models.CharField(max_length=5)),
                ('TipoLicor', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='tiposLicores.tiposlicores')),
            ],
        ),
        migrations.CreateModel(
            name='RegistroCompra',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('idBuy', models.UUIDField(default=uuid.uuid4, editable=False, unique=True)),
                ('idUser', models.CharField(max_length=30)),
                ('fullName', models.CharField(max_length=40)),
                ('email', models.CharField(max_length=40)),
                ('departament', models.CharField(max_length=20)),
                ('city', models.CharField(max_length=20)),
                ('address', models.CharField(max_length=40)),
                ('phone', models.CharField(max_length=40)),
                ('value', models.CharField(max_length=12)),
                ('idProduct', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='tienda.producto')),
                ('typeDocument', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='tiposDocumento.tiposdocumento')),
            ],
        ),
    ]
