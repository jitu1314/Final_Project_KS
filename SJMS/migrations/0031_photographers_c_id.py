# Generated by Django 2.2.2 on 2020-05-30 11:04

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('SJMS', '0030_photographers_p_desc'),
    ]

    operations = [
        migrations.AddField(
            model_name='photographers',
            name='c_id',
            field=models.ForeignKey(default=-1, on_delete=django.db.models.deletion.CASCADE, to='SJMS.category'),
            preserve_default=False,
        ),
    ]
