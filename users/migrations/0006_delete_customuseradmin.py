# Generated by Django 4.2.7 on 2024-12-29 13:17

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0005_initial'),
    ]

    operations = [
        migrations.DeleteModel(
            name='CustomUserAdmin',
        ),
    ]
