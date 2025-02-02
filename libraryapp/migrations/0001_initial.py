# Generated by Django 5.1.2 on 2024-10-23 12:52

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Author",
            fields=[
                ("author_id", models.IntegerField(primary_key=True, serialize=False)),
                ("pseudonym", models.CharField(blank=True, max_length=20, null=True)),
                (
                    "name_field",
                    models.CharField(
                        blank=True, db_column="name_", max_length=20, null=True
                    ),
                ),
                ("surname", models.CharField(blank=True, max_length=20, null=True)),
                ("country", models.CharField(blank=True, max_length=20, null=True)),
            ],
            options={
                "db_table": "author",
                "managed": False,
            },
        ),
        migrations.CreateModel(
            name="Shop",
            fields=[
                ("shop_id", models.IntegerField(primary_key=True, serialize=False)),
                ("town", models.CharField(max_length=20)),
                ("adress", models.CharField(max_length=30, unique=True)),
                ("hotline", models.IntegerField(blank=True, null=True, unique=True)),
            ],
            options={
                "db_table": "shop",
                "managed": False,
            },
        ),
        migrations.CreateModel(
            name="Book",
            fields=[
                ("book_id", models.AutoField(primary_key=True, serialize=False)),
                ("name_field", models.CharField(db_column="name_", max_length=50)),
                ("price_uah", models.IntegerField(db_column="price_UAH")),
                ("pages", models.IntegerField()),
            ],
            options={
                "db_table": "book",
                "managed": False,
            },
        ),
        migrations.CreateModel(
            name="Feedback",
            fields=[
                ("feedback_id", models.AutoField(primary_key=True, serialize=False)),
                ("feedback", models.CharField(max_length=200)),
                ("rating", models.IntegerField()),
            ],
            options={
                "db_table": "feedback",
                "managed": False,
            },
        ),
        migrations.CreateModel(
            name="Genre",
            fields=[
                ("genre_id", models.AutoField(primary_key=True, serialize=False)),
                ("genre_name", models.CharField(max_length=50, unique=True)),
            ],
            options={
                "db_table": "genre",
                "managed": False,
            },
        ),
        migrations.CreateModel(
            name="Purchases",
            fields=[
                ("purchase_id", models.AutoField(primary_key=True, serialize=False)),
                ("purchase_date", models.DateField()),
            ],
            options={
                "db_table": "purchases",
                "managed": False,
            },
        ),
        migrations.CreateModel(
            name="Reader",
            fields=[
                ("reader_id", models.AutoField(primary_key=True, serialize=False)),
                ("name_field", models.CharField(db_column="name_", max_length=20)),
                ("surname", models.CharField(max_length=20)),
            ],
            options={
                "db_table": "reader",
                "managed": False,
            },
        ),
        migrations.CreateModel(
            name="AuthorBook",
            fields=[
                (
                    "author",
                    models.OneToOneField(
                        on_delete=django.db.models.deletion.DO_NOTHING,
                        primary_key=True,
                        serialize=False,
                        to="libraryapp.author",
                    ),
                ),
            ],
            options={
                "db_table": "author_book",
                "managed": False,
            },
        ),
        migrations.CreateModel(
            name="AvailableBooks",
            fields=[
                (
                    "shop",
                    models.OneToOneField(
                        on_delete=django.db.models.deletion.DO_NOTHING,
                        primary_key=True,
                        serialize=False,
                        to="libraryapp.shop",
                    ),
                ),
                ("stock_quantity", models.IntegerField()),
            ],
            options={
                "db_table": "available_books",
                "managed": False,
            },
        ),
        migrations.CreateModel(
            name="BookGenre",
            fields=[
                (
                    "book",
                    models.OneToOneField(
                        on_delete=django.db.models.deletion.DO_NOTHING,
                        primary_key=True,
                        serialize=False,
                        to="libraryapp.book",
                    ),
                ),
            ],
            options={
                "db_table": "book_genre",
                "managed": False,
            },
        ),
    ]
