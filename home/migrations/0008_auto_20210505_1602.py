# Generated by Django 3.1.2 on 2021-05-05 16:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0007_auto_20210505_1515'),
    ]

    operations = [
        migrations.AlterField(
            model_name='medorganization',
            name='photo',
            field=models.ImageField(null=True, upload_to=''),
        ),
    ]