# Generated by Django 3.0.3 on 2020-06-10 01:24

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('admin_repartidor', '0002_auto_20200501_0238'),
        ('cliente', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='RepartidorOrden',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('orden', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cliente.Orden')),
                ('repartidor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='admin_repartidor.Repartidor')),
            ],
        ),
    ]
