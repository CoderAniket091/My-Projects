# Generated by Django 4.0.4 on 2022-05-21 09:44

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_user'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='User',
            new_name='UserMain',
        ),
    ]
