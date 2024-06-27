# Generated by Django 5.0.6 on 2024-06-27 10:16

import django.contrib.postgres.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Book",
            fields=[
                (
                    "isbn",
                    models.CharField(max_length=13, primary_key=True, serialize=False),
                ),
                ("title", models.CharField(max_length=50)),
                ("description", models.TextField(blank=True, null=True)),
                ("page_count", models.PositiveSmallIntegerField()),
                (
                    "catgegory",
                    models.CharField(
                        choices=[
                            ("pr", "programming"),
                            ("ar", "art"),
                            ("hi", "history"),
                            ("po", "politics"),
                            ("ot", "others"),
                        ],
                        default="pr",
                        max_length=2,
                    ),
                ),
                ("published_date", models.IntegerField()),
                ("publisher", models.CharField(max_length=50)),
                (
                    "authors",
                    django.contrib.postgres.fields.ArrayField(
                        base_field=django.contrib.postgres.fields.ArrayField(
                            base_field=models.CharField(max_length=50), size=None
                        ),
                        size=None,
                    ),
                ),
                ("language", models.CharField(max_length=50)),
                ("edition", models.SmallIntegerField(blank=True, null=True)),
                (
                    "book_format",
                    models.CharField(
                        choices=[("eb", "ebook"), ("hc", "hardcover")],
                        default="eb",
                        max_length=2,
                    ),
                ),
            ],
        ),
    ]
