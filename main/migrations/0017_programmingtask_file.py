# Generated by Django 2.2.8 on 2022-06-04 22:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0016_auto_20220525_2133'),
    ]

    operations = [
        migrations.AddField(
            model_name='programmingtask',
            name='file',
            field=models.FileField(blank=True, null=True, upload_to=''),
        ),
    ]
