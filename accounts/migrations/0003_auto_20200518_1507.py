# Generated by Django 3.0.5 on 2020-05-18 09:22

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0002_auto_20200518_1300'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='studentlogin',
            options={},
        ),
        migrations.RemoveField(
            model_name='studentlogin',
            name='roll',
        ),
    ]