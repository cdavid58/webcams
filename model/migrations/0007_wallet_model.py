# Generated by Django 3.2.8 on 2022-08-24 20:15

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('model', '0006_alter_modelo_tags'),
    ]

    operations = [
        migrations.CreateModel(
            name='Wallet_Model',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('amount', models.IntegerField()),
                ('modelo', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='model.modelo')),
            ],
        ),
    ]
