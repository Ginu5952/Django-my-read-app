# Generated by Django 5.0.6 on 2024-07-10 09:54

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("reader", "0005_alter_nic_table_comment"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="nic",
            options={"verbose_name_plural": "NIC"},
        ),
    ]
