# Generated by Django 5.0.6 on 2024-07-10 09:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("book", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="book",
            name="created_at",
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AddField(
            model_name="book",
            name="modified_at",
            field=models.DateTimeField(auto_now=True),
        ),
    ]
