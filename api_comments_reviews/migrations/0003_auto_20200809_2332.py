# Generated by Django 3.0.5 on 2020-08-09 18:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api_comments_reviews', '0002_auto_20200809_2201'),
    ]

    operations = [
        migrations.AlterField(
            model_name='review',
            name='score',
            field=models.PositiveSmallIntegerField(),
        ),
    ]
