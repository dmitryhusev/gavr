# Generated by Django 4.2.5 on 2023-11-18 23:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='body',
            field=models.TextField(blank=True, max_length=255, null=True),
        ),
    ]
