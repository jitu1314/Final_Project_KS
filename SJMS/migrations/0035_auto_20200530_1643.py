# Generated by Django 2.2.2 on 2020-05-30 11:13

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('SJMS', '0034_auto_20200530_1642'),
    ]

    operations = [
        migrations.RenameField(
            model_name='photographers',
            old_name='p_descp',
            new_name='p_desc',
        ),
    ]