# Generated by Django 2.1 on 2018-08-23 15:09

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('blat', '0009_auto_20180822_1411'),
    ]

    operations = [
        migrations.CreateModel(
            name='PaymentPlan',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('planName', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='ProductCategory',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('catergory_name', models.CharField(max_length=50)),
                ('Quantity', models.IntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='Supplier',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('company_name', models.CharField(max_length=50)),
                ('contact_name', models.CharField(max_length=50)),
                ('address', models.CharField(max_length=50)),
                ('county', models.CharField(max_length=50)),
                ('phone', models.CharField(max_length=50)),
                ('website', models.CharField(max_length=50)),
            ],
        ),
        migrations.RemoveField(
            model_name='product',
            name='Quantity',
        ),
        migrations.AddField(
            model_name='customer',
            name='country',
            field=models.CharField(default='Uganda', max_length=50),
        ),
        migrations.AddField(
            model_name='payment',
            name='paymentType',
            field=models.CharField(choices=[('cash', 'CASH'), ('mobileMoney', 'MOBILE MONEY')], default='cash', max_length=20),
        ),
        migrations.AddField(
            model_name='product',
            name='buyPrice',
            field=models.FloatField(default=0),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='product',
            name='sellPrice',
            field=models.FloatField(default=0),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='customer',
            name='paymentPlan',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='blat.PaymentPlan'),
        ),
        migrations.AddField(
            model_name='product',
            name='catergory_name',
            field=models.ForeignKey(default=500, on_delete=django.db.models.deletion.CASCADE, to='blat.ProductCategory'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='product',
            name='supplier_name',
            field=models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, to='blat.Supplier'),
            preserve_default=False,
        ),
    ]
