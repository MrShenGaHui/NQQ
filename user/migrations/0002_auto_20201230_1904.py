# Generated by Django 2.2.12 on 2020-12-30 11:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='addrprofile',
            name='postcode',
            field=models.IntegerField(verbose_name='邮编'),
        ),
    ]
