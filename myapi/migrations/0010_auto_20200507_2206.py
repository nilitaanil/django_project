# Generated by Django 2.2.12 on 2020-05-07 16:36

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('myapi', '0009_auto_20200507_2017'),
    ]

    operations = [
        migrations.AlterField(
            model_name='period',
            name='member',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='period_def', to='myapi.Member'),
        ),
    ]
