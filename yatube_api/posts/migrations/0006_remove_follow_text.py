# Generated by Django 2.2.16 on 2022-06-05 23:12

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0005_follow_text'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='follow',
            name='text',
        ),
    ]
