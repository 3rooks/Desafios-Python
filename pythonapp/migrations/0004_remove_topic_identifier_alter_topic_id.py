# Generated by Django 4.0.4 on 2022-05-27 05:05

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('pythonapp', '0003_remove_topic_updated_topic_identifier'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='topic',
            name='identifier',
        ),
        migrations.AlterField(
            model_name='topic',
            name='id',
            field=models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False),
        ),
    ]
