# Generated by Django 3.0 on 2019-12-30 13:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='project',
            name='slug',
            field=models.SlugField(max_length=100, null=True),
        ),
    ]
