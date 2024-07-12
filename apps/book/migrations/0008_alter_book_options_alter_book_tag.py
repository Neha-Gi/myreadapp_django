# Generated by Django 5.0.6 on 2024-07-10 09:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("book", "0007_book_created_at_book_modified_at"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="book",
            options={"default_related_name": "%(app_label)s_%(model_name)s"},
        ),
        migrations.AlterField(
            model_name="book",
            name="tag",
            field=models.ManyToManyField(to="book.tag"),
        ),
    ]
