# Generated by Django 5.0.6 on 2024-07-04 08:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("book", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="author",
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
                ("first_name", models.CharField(blank=True, max_length=100, null=True)),
                ("last_name", models.CharField(blank=True, max_length=100, null=True)),
            ],
        ),
    ]
