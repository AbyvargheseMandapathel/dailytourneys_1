# Generated by Django 4.1.2 on 2022-10-19 11:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ads', '0032_adstopbanner_url'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ads',
            name='prize',
            field=models.CharField(max_length=200),
        ),
    ]