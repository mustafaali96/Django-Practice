# Generated by Django 3.1.4 on 2020-12-30 07:00

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('custom_app', '0012_auto_20201230_1132'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='subject',
        ),
        migrations.AddField(
            model_name='user',
            name='subject',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='custom_app.courses'),
        ),
    ]