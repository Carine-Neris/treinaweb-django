# Generated by Django 2.2.1 on 2019-05-30 17:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('clientes', '0006_auto_20190530_1452'),
    ]

    operations = [
        migrations.AlterField(
            model_name='produto',
            name='preco',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=7),
        ),
    ]