# Generated by Django 4.0.4 on 2022-06-13 15:57

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pythonapp', '0007_topic_created_by'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='topic',
            name='created_by',
        ),
    ]
