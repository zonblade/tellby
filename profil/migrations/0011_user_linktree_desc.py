# Generated by Django 3.1.4 on 2020-12-14 02:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('profil', '0010_user_linktree_mock'),
    ]

    operations = [
        migrations.AddField(
            model_name='user_linktree',
            name='desc',
            field=models.CharField(blank=True, default='#', max_length=300, null=True),
        ),
    ]
