# Generated by Django 3.1.4 on 2020-12-27 10:50

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='thread',
            name='first',
        ),
        migrations.RemoveField(
            model_name='thread',
            name='second',
        ),
        migrations.DeleteModel(
            name='ChatMessage',
        ),
        migrations.DeleteModel(
            name='Thread',
        ),
    ]
