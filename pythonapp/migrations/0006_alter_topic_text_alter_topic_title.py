# Generated by Django 4.0.4 on 2022-06-02 00:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pythonapp', '0005_rename_topic_topic_title_alter_topic_text'),
    ]

    operations = [
        migrations.AlterField(
            model_name='topic',
            name='text',
            field=models.TextField(max_length=1000),
        ),
        migrations.AlterField(
            model_name='topic',
            name='title',
            field=models.CharField(max_length=50),
        ),
    ]
