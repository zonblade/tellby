# Generated by Django 3.1.4 on 2020-12-11 08:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('postingan', '0006_auto_20201211_1528'),
    ]

    operations = [
        migrations.AlterField(
            model_name='postingan',
            name='user_id',
            field=models.DecimalField(decimal_places=0, max_digits=50),
        ),
    ]
