# Generated by Django 2.2.2 on 2020-05-30 09:04

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('SJMS', '0016_photographer_p_amt'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='photographer',
            name='p_desc',
        ),
        migrations.AddField(
            model_name='photographer',
            name='c_id',
            field=models.ForeignKey(default=-1, on_delete=django.db.models.deletion.CASCADE, to='SJMS.category'),
            preserve_default=False,
        ),
    ]