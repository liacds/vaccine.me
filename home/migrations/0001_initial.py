# Generated by Django 3.1.2 on 2021-04-10 06:56

from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='MedOrganization',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('address', models.CharField(max_length=255)),
                ('in_stock', models.BooleanField(default=True)),
                ('has_type_1', models.BooleanField(default=True)),
                ('has_type_2', models.BooleanField(default=True)),
                ('schedule_weekday', models.CharField(max_length=255)),
                ('schedule_time', models.CharField(max_length=255)),
                ('phone_number', models.IntegerField()),
                ('website', models.URLField(max_length=128, null=True)),
                ('twogis_link', models.URLField(max_length=128, null=True)),
                ('rayon', models.CharField(max_length=255)),
                ('photo', models.ImageField(upload_to='')),
                ('documents_needed', models.CharField(max_length=255)),
            ],
        ),
    ]
