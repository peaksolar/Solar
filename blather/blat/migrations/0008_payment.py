# Generated by Django 2.1 on 2018-08-22 19:08

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('blat', '0007_auto_20180822_1038'),
    ]

    operations = [
        migrations.CreateModel(
            name='Payment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('paymentDate', models.DateTimeField(auto_now_add=True)),
                ('amount', models.IntegerField()),
                ('customerName', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='blat.Customer')),
                ('payGID', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='blat.Product')),
            ],
        ),
    ]
