# Generated by Django 4.0.4 on 2022-05-21 11:27

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='FollowData',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username1', models.CharField(max_length=100)),
                ('username2', models.CharField(max_length=100)),
            ],
        ),
    ]