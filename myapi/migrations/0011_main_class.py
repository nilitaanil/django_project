# Generated by Django 2.2.12 on 2020-05-07 16:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapi', '0010_auto_20200507_2206'),
    ]

    operations = [
        migrations.CreateModel(
            name='main_class',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ok', models.BooleanField()),
            ],
        ),
    ]
