# Generated by Django 3.1.4 on 2020-12-13 18:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('profil', '0009_auto_20201214_0134'),
    ]

    operations = [
        migrations.AddField(
            model_name='user_linktree',
            name='mock',
            field=models.CharField(blank=True, max_length=300, null=True),
        ),
    ]
