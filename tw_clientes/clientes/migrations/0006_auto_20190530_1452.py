# Generated by Django 2.2.1 on 2019-05-30 17:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('clientes', '0005_auto_20190515_1552'),
    ]

    operations = [
        migrations.AlterField(
            model_name='produto',
            name='preco',
            field=models.DecimalField(decimal_places=2, max_digits=7),
        ),
    ]
