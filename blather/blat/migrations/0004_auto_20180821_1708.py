# Generated by Django 2.1 on 2018-08-21 22:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blat', '0003_auto_20180821_1704'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tokens',
            name='tokenID',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
    ]