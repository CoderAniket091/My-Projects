# Generated by Django 4.0.4 on 2022-05-02 10:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0004_usercart_delete_customercart'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='usercart',
            name='Bookid',
        ),
        migrations.RemoveField(
            model_name='usercart',
            name='Userid',
        ),
        migrations.AddField(
            model_name='usercart',
            name='bookID',
            field=models.IntegerField(default=12),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='usercart',
            name='userID',
            field=models.IntegerField(default=12),
            preserve_default=False,
        ),
    ]
