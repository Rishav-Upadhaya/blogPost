# Generated by Django 4.2.7 on 2024-12-26 14:13

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blogs', '0002_title_alter_blog_title'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Title',
            new_name='Name',
        ),
    ]
