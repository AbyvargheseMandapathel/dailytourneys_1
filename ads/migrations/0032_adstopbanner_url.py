# Generated by Django 3.2.13 on 2022-10-16 15:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ads', '0031_auto_20221016_1422'),
    ]

    operations = [
        migrations.AddField(
            model_name='adstopbanner',
            name='url',
            field=models.CharField(blank=True, default='Enter the Url', max_length=200),
        ),
    ]
