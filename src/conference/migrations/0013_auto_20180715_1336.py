# Generated by Django 2.1a1 on 2018-07-15 08:06

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('conference', '0012_auto_20180715_1125'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='reviewpaper',
            name='currentUser',
        ),
        migrations.RemoveField(
            model_name='reviewpaper',
            name='paper',
        ),
        migrations.RenameField(
            model_name='commentonpaper',
            old_name='commentuser',
            new_name='user',
        ),
        migrations.DeleteModel(
            name='reviewPaper',
        ),
    ]
