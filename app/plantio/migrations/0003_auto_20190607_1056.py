# Generated by Django 2.2.2 on 2019-06-07 15:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('plantio', '0002_auto_20190607_1055'),
    ]

    operations = [
        migrations.AlterField(
            model_name='plantio',
            name='estado',
            field=models.CharField(choices=[('planejado', 'planejado'), ('plantado', 'plantado'), ('finalizado/removido', 'finalizado/removido')], max_length=20, verbose_name='estado'),
        ),
    ]