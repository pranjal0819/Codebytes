# Generated by Django 2.1a1 on 2018-07-14 07:37

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('conference', '0003_auto_20180714_1203'),
    ]

    operations = [
        migrations.AddField(
            model_name='reviewpaper',
            name='currentUser',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.PROTECT, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='reviewpaper',
            name='paper',
            field=models.ManyToManyField(to='conference.paperRecord'),
        ),
    ]