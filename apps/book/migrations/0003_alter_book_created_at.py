# Generated by Django 5.0.6 on 2024-07-10 09:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("book", "0002_book_created_at_book_modified_at"),
    ]

    operations = [
        migrations.AlterField(
            model_name="book",
            name="created_at",
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]