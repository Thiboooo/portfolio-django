# Generated by Django 3.0 on 2019-12-30 18:31

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '0005_auto_20191230_1831'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='project',
            name='image',
        ),
    ]