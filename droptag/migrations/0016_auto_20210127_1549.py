# Generated by Django 3.0.8 on 2021-01-27 20:49

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('droptag', '0015_remove_userprofile_slug'),
    ]

    operations = [
        migrations.RenameField(
            model_name='userprofile',
            old_name='user',
            new_name='username',
        ),
    ]
