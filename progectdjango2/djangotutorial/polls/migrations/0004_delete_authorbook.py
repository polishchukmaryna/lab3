# Generated by Django 5.1.2 on 2024-11-01 14:57

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("polls", "0003_authorbook"),
    ]

    operations = [
        migrations.DeleteModel(
            name="AuthorBook",
        ),
    ]