# Generated by Django 4.2.7 on 2024-12-28 14:41

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_rename_createuserform_form'),
    ]

    operations = [
        migrations.RenameField(
            model_name='form',
            old_name='password1',
            new_name='password',
        ),
        migrations.RenameField(
            model_name='form',
            old_name='user',
            new_name='username',
        ),
    ]
