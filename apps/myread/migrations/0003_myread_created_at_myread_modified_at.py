# Generated by Django 5.0.6 on 2024-07-11 07:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("myread", "0002_alter_myread_unique_together"),
    ]

    operations = [
        migrations.AddField(
            model_name="myread",
            name="created_at",
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
        migrations.AddField(
            model_name="myread",
            name="modified_at",
            field=models.DateTimeField(auto_now=True, null=True),
        ),
    ]