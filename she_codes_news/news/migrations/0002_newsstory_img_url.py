# Generated by Django 3.2.5 on 2021-08-19 10:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='newsstory',
            name='img_url',
            field=models.URLField(default='https://placedog.net/500/280'),
        ),
    ]
