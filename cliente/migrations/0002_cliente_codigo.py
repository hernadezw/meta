# Generated by Django 4.1.5 on 2023-01-13 04:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cliente', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='cliente',
            name='codigo',
            field=models.IntegerField(auto_created=True, default=None),
            preserve_default=False,
        ),
    ]
