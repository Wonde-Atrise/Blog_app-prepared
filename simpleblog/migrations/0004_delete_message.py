# Generated by Django 5.1.5 on 2025-02-11 18:54

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('simpleblog', '0003_rename_messagebody_message'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Message',
        ),
    ]
