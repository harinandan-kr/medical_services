# Generated by Django 3.2.6 on 2021-08-08 05:23

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('display', '0011_auto_20210807_1643'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='laboratory',
            name='laboratory_deposit',
        ),
        migrations.RemoveField(
            model_name='laboratory',
            name='laboratory_mealtype',
        ),
        migrations.RemoveField(
            model_name='laboratory',
            name='laboratory_mess',
        ),
        migrations.RemoveField(
            model_name='laboratory',
            name='laboratory_rent',
        ),
    ]
