# Generated by Django 2.1a1 on 2018-07-23 20:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('conference', '0014_review'),
    ]

    operations = [
        migrations.AddField(
            model_name='review',
            name='comment',
            field=models.TextField(default=None),
        ),
    ]
