# Generated by Django 2.2.12 on 2020-05-07 07:25

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('myapi', '0004_auto_20200507_1238'),
    ]

    operations = [
        migrations.AddField(
            model_name='member',
            name='end',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='member',
            name='start',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
        migrations.DeleteModel(
            name='Period',
        ),
    ]
