# Generated by Django 3.1.4 on 2020-12-30 11:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('custom_app', '0017_auto_20201230_1624'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='subject',
            field=models.ManyToManyField(to='custom_app.Courses'),
        ),
    ]