# Generated by Django 3.1.4 on 2020-12-11 14:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('postingan', '0007_auto_20201211_1529'),
    ]

    operations = [
        migrations.CreateModel(
            name='Komentar',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('post_id', models.DecimalField(decimal_places=0, max_digits=50)),
                ('user_id', models.DecimalField(decimal_places=0, max_digits=50)),
                ('komen_date', models.DateTimeField(auto_now_add=True)),
                ('komen', models.TextField()),
            ],
        ),
    ]
