# Generated by Django 2.2.2 on 2020-04-25 08:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('SJMS', '0010_auto_20200417_1629'),
    ]

    operations = [
        migrations.AddField(
            model_name='photographer',
            name='p_otp',
            field=models.CharField(default=-1, max_length=10),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='photographer',
            name='p_otp_used',
            field=models.IntegerField(default=-1),
            preserve_default=False,
        ),
    ]
