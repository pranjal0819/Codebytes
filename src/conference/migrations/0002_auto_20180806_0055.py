# Generated by Django 2.1a1 on 2018-08-05 19:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('conference', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='paperrecord',
            name='status',
            field=models.IntegerField(default=3),
        ),
    ]
