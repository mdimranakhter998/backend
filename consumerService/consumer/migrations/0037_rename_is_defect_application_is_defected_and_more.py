# Generated by Django 4.1.1 on 2022-11-28 09:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('consumer', '0036_alter_verify_remark'),
    ]

    operations = [
        migrations.RenameField(
            model_name='application',
            old_name='is_defect',
            new_name='is_defected',
        ),
        migrations.AddField(
            model_name='application',
            name='is_rejected',
            field=models.BooleanField(default=False),
        ),
    ]
