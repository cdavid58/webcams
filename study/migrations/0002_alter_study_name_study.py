# Generated by Django 3.2.8 on 2022-08-24 17:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('study', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='study',
            name='name_study',
            field=models.CharField(max_length=40, unique=True),
        ),
    ]
