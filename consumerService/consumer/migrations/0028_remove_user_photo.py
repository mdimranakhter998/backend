# Generated by Django 4.1.1 on 2022-11-18 16:24

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('consumer', '0027_user_photo'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='photo',
        ),
    ]
