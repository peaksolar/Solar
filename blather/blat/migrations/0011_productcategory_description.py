# Generated by Django 2.1 on 2018-08-23 15:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blat', '0010_auto_20180823_1009'),
    ]

    operations = [
        migrations.AddField(
            model_name='productcategory',
            name='description',
            field=models.CharField(default=0, max_length=100),
            preserve_default=False,
        ),
    ]
