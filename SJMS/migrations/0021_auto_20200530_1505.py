# Generated by Django 2.2.2 on 2020-05-30 09:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('SJMS', '0020_ppp'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='photographer',
            name='c_id',
        ),
        migrations.AddField(
            model_name='photographer',
            name='p_desc',
            field=models.CharField(default=-1, max_length=200),
            preserve_default=False,
        ),
    ]
