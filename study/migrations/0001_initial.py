# Generated by Django 3.2.8 on 2022-08-18 19:57

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Study',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name_study', models.CharField(max_length=40)),
                ('pswd', models.CharField(max_length=20)),
                ('email', models.EmailField(max_length=254, unique=True)),
                ('birthday', models.CharField(max_length=12)),
                ('block', models.BooleanField(default=False)),
                ('independent', models.BooleanField(default=False)),
            ],
        ),
    ]
