# Generated by Django 2.2.2 on 2020-02-01 04:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('SJMS', '0002_contactus'),
    ]

    operations = [
        migrations.AddField(
            model_name='contactus',
            name='cn_name',
            field=models.CharField(default=-1, max_length=50),
            preserve_default=False,
        ),
    ]