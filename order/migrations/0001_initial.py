# Generated by Django 2.2.12 on 2020-12-30 11:26

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('user', '0002_auto_20201230_1904'),
    ]

    operations = [
        migrations.CreateModel(
            name='OrderProfile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('payment_method', models.CharField(max_length=20, verbose_name='支付方式')),
                ('totalQty', models.IntegerField(verbose_name='总数目')),
                ('total_cost', models.DecimalField(decimal_places=2, max_digits=10, verbose_name='总金额')),
                ('freight', models.DecimalField(decimal_places=2, max_digits=10, verbose_name='运费')),
                ('payment_status', models.IntegerField(verbose_name='支付状态')),
                ('created_time', models.DateTimeField(auto_now_add=True, verbose_name='创建时间')),
                ('addr_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='user.AddrProfile')),
                ('user_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='user.UserProfile')),
            ],
        ),
    ]
