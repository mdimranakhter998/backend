# Generated by Django 4.1.1 on 2022-11-18 13:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('consumer', '0014_remove_user_photo_user_phone'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='photo',
            field=models.ImageField(blank=True, null=True, upload_to='user/'),
        ),
    ]
