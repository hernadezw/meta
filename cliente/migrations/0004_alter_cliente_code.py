# Generated by Django 4.1.5 on 2023-01-13 05:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cliente', '0003_remove_cliente_codigo_cliente_code'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cliente',
            name='code',
            field=models.CharField(auto_created=True, max_length=10, unique=True, verbose_name='Code'),
        ),
    ]
