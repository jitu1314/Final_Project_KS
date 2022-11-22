# Generated by Django 2.2.2 on 2020-06-05 08:34

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('SJMS', '0038_delete_cat'),
    ]

    operations = [
        migrations.AddField(
            model_name='photographers',
            name='c_id',
            field=models.ForeignKey(default=-1, on_delete=django.db.models.deletion.CASCADE, to='SJMS.category'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='photographers',
            name='pay_status',
            field=models.IntegerField(default=0, max_length=2),
        ),
        migrations.AlterField(
            model_name='feedback',
            name='f_date',
            field=models.DateField(),
        ),
        migrations.AlterField(
            model_name='photographers',
            name='p_contact',
            field=models.CharField(max_length=10),
        ),
        migrations.AlterField(
            model_name='users',
            name='contact',
            field=models.CharField(max_length=10),
        ),
    ]