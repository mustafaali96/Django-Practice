# Generated by Django 3.1.4 on 2020-12-30 07:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('custom_app', '0015_auto_20201230_1217'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='subject',
        ),
        migrations.AddField(
            model_name='user',
            name='subject',
            field=models.ManyToManyField(to='custom_app.Courses'),
        ),
    ]
