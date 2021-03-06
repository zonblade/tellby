# Generated by Django 3.1.4 on 2020-12-13 18:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('profil', '0008_user_linktree'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user_linktree',
            name='img',
            field=models.CharField(blank=True, default='https://cdn.tell.by/img/icon/eucalyptus.png', max_length=300, null=True),
        ),
        migrations.AlterField(
            model_name='user_linktree',
            name='link',
            field=models.CharField(blank=True, default='#', max_length=300, null=True),
        ),
        migrations.AlterField(
            model_name='user_linktree',
            name='order',
            field=models.CharField(blank=True, default='0', max_length=300, null=True),
        ),
        migrations.AlterField(
            model_name='user_linktree',
            name='title',
            field=models.CharField(blank=True, default='#', max_length=300, null=True),
        ),
    ]
