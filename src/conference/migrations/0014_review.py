# Generated by Django 2.1a1 on 2018-07-23 19:59

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('conference', '0013_auto_20180715_1336'),
    ]

    operations = [
        migrations.CreateModel(
            name='review',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('paper', models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, related_name='paper', to='conference.paperRecord')),
                ('user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, related_name='user', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
