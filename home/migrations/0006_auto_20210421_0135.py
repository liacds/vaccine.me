# Generated by Django 3.1.2 on 2021-04-21 01:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0005_auto_20210411_1600'),
    ]

    operations = [
        migrations.AlterField(
            model_name='medorganization',
            name='extra',
            field=models.CharField(max_length=255),
        ),
    ]
