# Generated by Django 3.2.8 on 2022-08-28 23:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0003_configuration_value_token_transaction'),
    ]

    operations = [
        migrations.AlterField(
            model_name='configuration',
            name='value_token_transaction',
            field=models.CharField(blank=True, max_length=150, null=True),
        ),
    ]
