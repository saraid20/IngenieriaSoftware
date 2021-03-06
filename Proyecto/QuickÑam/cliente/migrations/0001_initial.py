# Generated by Django 3.0.3 on 2020-06-09 20:14

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('admin_alimentos', '0002_auto_20200430_0350'),
        ('usuarios', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Carrito',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fecha', models.DateTimeField(default=datetime.datetime.now)),
                ('completado', models.BooleanField(default=False)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Orden',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('order_id', models.CharField(default='abc', max_length=120, unique=True)),
                ('estado', models.IntegerField(blank=True, choices=[(0, 'Recibido'), (1, 'Listo para entregar'), (2, 'En proceso de entrega'), (3, 'Entregado')], default=0)),
                ('fecha', models.DateTimeField(auto_now_add=True)),
                ('total', models.DecimalField(decimal_places=2, default=1000.0, max_digits=300)),
                ('carrito', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cliente.Carrito')),
                ('ubicacion', models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, to='usuarios.Ubicacion')),
                ('user', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='usuarios.Cliente')),
            ],
        ),
        migrations.CreateModel(
            name='ArticuloCarrito',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cantidad', models.IntegerField(default=1)),
                ('precio', models.FloatField(blank=True)),
                ('carrito', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cliente.Carrito')),
                ('producto', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='admin_alimentos.Alimento')),
            ],
        ),
    ]
