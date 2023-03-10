# Generated by Django 4.1.1 on 2022-11-16 12:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('consumer', '0011_remove_application_photo_user_photo'),
    ]

    operations = [
        migrations.AddField(
            model_name='application',
            name='photo',
            field=models.ImageField(blank=True, null=True, upload_to='applicant/'),
        ),
        migrations.AlterField(
            model_name='user',
            name='photo',
            field=models.ImageField(blank=True, null=True, upload_to='user/'),
        ),
    ]
