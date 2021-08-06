# Generated by Django 3.1.4 on 2020-12-25 08:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('postingan', '0011_remove_postingan_pop_count'),
    ]

    operations = [
        migrations.CreateModel(
            name='Prefered_Template',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_id', models.DecimalField(decimal_places=0, max_digits=50)),
                ('template_type', models.DecimalField(decimal_places=0, default=1, max_digits=50)),
            ],
        ),
        migrations.AddField(
            model_name='postingan',
            name='post_keyword',
            field=models.TextField(blank=True, default='Tell By Story', null=True),
        ),
        migrations.AddField(
            model_name='postingan',
            name='post_title',
            field=models.CharField(default='Story', max_length=50),
        ),
    ]