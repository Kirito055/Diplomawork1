# Generated by Django 2.2.8 on 2022-05-25 13:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0014_auto_20220525_1842'),
    ]

    operations = [
        migrations.AddField(
            model_name='programmingtask',
            name='rating',
            field=models.IntegerField(default=0),
        ),
    ]
