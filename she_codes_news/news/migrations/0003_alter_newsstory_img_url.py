# Generated by Django 3.2.5 on 2021-08-20 07:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0002_newsstory_img_url'),
    ]

    operations = [
        migrations.AlterField(
            model_name='newsstory',
            name='img_url',
            field=models.URLField(default='https://placebear.com/200/300'),
        ),
    ]
