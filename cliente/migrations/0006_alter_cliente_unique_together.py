# Generated by Django 4.1.5 on 2023-01-13 05:53

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cliente', '0005_alter_cliente_code'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='cliente',
            unique_together=set(),
        ),
    ]
