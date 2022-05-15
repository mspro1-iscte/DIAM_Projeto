# Generated by Django 4.0.3 on 2022-05-15 18:35

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('loja', '0012_merge_0009_alter_produto_foto_rating_0011_rating'),
    ]

    operations = [
        migrations.CreateModel(
            name='Compras',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('total', models.DecimalField(decimal_places=2, max_digits=5)),
                ('date', models.DateField(default=datetime.datetime(2022, 5, 15, 19, 35, 9, 698553))),
                ('cliente', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='loja.cliente')),
                ('produtos', models.ManyToManyField(blank=True, null=True, to='loja.produto')),
            ],
        ),
    ]
