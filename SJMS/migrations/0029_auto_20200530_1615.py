# Generated by Django 2.2.2 on 2020-05-30 10:45

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('SJMS', '0028_auto_20200530_1608'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='photographers',
            name='p_desc',
        ),
        migrations.AlterModelTable(
            name='photographers',
            table='photographer',
        ),
    ]
