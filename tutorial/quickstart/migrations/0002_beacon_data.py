# Generated by Django 2.2.7 on 2020-02-01 07:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('quickstart', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='beacon',
            name='data',
            field=models.CharField(default='', max_length=512),
        ),
    ]
