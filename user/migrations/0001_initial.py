# Generated by Django 2.2.12 on 2020-12-30 10:59

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='UserProfile',
            fields=[
                ('username', models.CharField(max_length=20, primary_key=True, serialize=False, verbose_name='用户名')),
                ('email', models.EmailField(max_length=254, verbose_name='邮箱')),
                ('password', models.CharField(max_length=32)),
                ('use_tel', models.CharField(default='', max_length=11, verbose_name='手机')),
            ],
        ),
        migrations.CreateModel(
            name='AddrProfile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('contact', models.CharField(max_length=30, verbose_name='收件人')),
                ('addr_tel', models.CharField(default='', max_length=11, verbose_name='手机号')),
                ('addr', models.CharField(max_length=100, verbose_name='地址')),
                ('postcode', models.IntegerField(max_length=6, verbose_name='邮编')),
                ('user_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='user.UserProfile')),
            ],
        ),
    ]
