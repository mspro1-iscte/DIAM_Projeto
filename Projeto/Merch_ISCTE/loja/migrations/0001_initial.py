# Generated by Django 4.0.4 on 2022-04-28 13:02

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Produto',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('produto_nome', models.CharField(max_length=50)),
                ('produto_texto', models.CharField(max_length=200)),
                ('preco_data', models.DecimalField(decimal_places=2, default=0.0, max_digits=5)),
                ('pub_data', models.DateTimeField(verbose_name='data de publicacao')),
                ('foto', models.CharField(default='/loja/static/media/avatardefault.png', max_length=100)),
            ],
        ),
    ]