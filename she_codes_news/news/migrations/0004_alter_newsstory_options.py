# Generated by Django 3.2.5 on 2021-08-21 00:25

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0003_alter_newsstory_img_url'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='newsstory',
            options={'ordering': ['-pub_date']},
        ),
    ]
