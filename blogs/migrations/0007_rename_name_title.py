# Generated by Django 4.2.7 on 2024-12-26 15:33

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blogs', '0006_name_alter_blog_title'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Name',
            new_name='Title',
        ),
    ]
