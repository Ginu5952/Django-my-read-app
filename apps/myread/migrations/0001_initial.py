# Generated by Django 5.0.6 on 2024-07-04 10:43

import django.contrib.postgres.fields.ranges
import django.contrib.postgres.validators
import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ("book", "0001_initial"),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name="StatusPercent",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "percentage_read_range",
                    django.contrib.postgres.fields.ranges.IntegerRangeField(
                        blank=True,
                        null=True,
                        validators=[
                            django.contrib.postgres.validators.RangeMinValueValidator(
                                0
                            ),
                            django.contrib.postgres.validators.RangeMaxValueValidator(
                                101
                            ),
                        ],
                    ),
                ),
                (
                    "read_status",
                    models.CharField(
                        choices=[
                            ("pending", "Pending"),
                            ("reading", "Reading"),
                            ("done", "Done"),
                        ],
                        default="pending",
                        max_length=10,
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="MyRead",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "percentage_read",
                    models.PositiveSmallIntegerField(blank=True, null=True),
                ),
                ("start_read_date", models.DateField(blank=True, null=True)),
                ("end_read_date", models.DateField(blank=True, null=True)),
                (
                    "book_isbn",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="book.book"
                    ),
                ),
                (
                    "reader_username",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
        ),
        migrations.AddConstraint(
            model_name="statuspercent",
            constraint=models.CheckConstraint(
                check=models.Q(("read_status__in", ["pending", "reading", "done"])),
                name="myread_statuspercent_read_status_check",
            ),
        ),
        migrations.AddConstraint(
            model_name="myread",
            constraint=models.CheckConstraint(
                check=models.Q(
                    ("percentage_read__gte", 0), ("percentage_read__lte", 100)
                ),
                name="myread_myread_per_read_check",
            ),
        ),
        migrations.AddConstraint(
            model_name="myread",
            constraint=models.CheckConstraint(
                check=models.Q(("end_read_date__gt", models.F("start_read_date"))),
                name="myread_myread_end_read_start_read_date_check",
            ),
        ),
        migrations.AddConstraint(
            model_name="myread",
            constraint=models.CheckConstraint(
                check=models.Q(
                    models.Q(
                        ("percentage_read__exact", 0), ("start_read_date__isnull", True)
                    ),
                    models.Q(
                        ("percentage_read__gt", 0), ("start_read_date__isnull", False)
                    ),
                    _connector="OR",
                ),
                name="myread_myread_per_read_start_read_date_check",
            ),
        ),
        migrations.AddConstraint(
            model_name="myread",
            constraint=models.CheckConstraint(
                check=models.Q(
                    models.Q(
                        ("end_read_date__isnull", False),
                        ("percentage_read__exact", 100),
                    ),
                    models.Q(
                        ("end_read_date__isnull", True), ("percentage_read__lt", 100)
                    ),
                    _connector="OR",
                ),
                name="myread_myread_per_read_end_read_date_check",
            ),
        ),
    ]
