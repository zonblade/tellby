# Generated by Django 3.1.4 on 2020-12-15 10:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gallery', '0003_auto_20201215_1750'),
    ]

    operations = [
        migrations.AlterField(
            model_name='image_gallery',
            name='user_id',
            field=models.DecimalField(decimal_places=0, default=0, max_digits=65),
        ),
    ]