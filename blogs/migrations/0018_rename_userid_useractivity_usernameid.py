# Generated by Django 4.2.7 on 2025-01-10 11:42

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blogs', '0017_rename_user_useractivity_userid'),
    ]

    operations = [
        migrations.RenameField(
            model_name='useractivity',
            old_name='userid',
            new_name='usernameid',
        ),
    ]
