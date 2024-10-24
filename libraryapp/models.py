from django.db import models

# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class Author(models.Model):
    author_id = models.IntegerField(primary_key=True)
    pseudonym = models.CharField(max_length=20, blank=True, null=True)
    name_field = models.CharField(db_column='name_', max_length=20, blank=True, null=True)  # Field renamed because it ended with '_'.
    surname = models.CharField(max_length=20, blank=True, null=True)
    country = models.CharField(max_length=20, blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'author'
    
    def __str__(self):
        return self.name_field


class AuthorBook(models.Model):
    author = models.OneToOneField(Author, models.DO_NOTHING, primary_key=True)  # The composite primary key (author_id, book_id) found, that is not supported. The first column is selected.
    book = models.ForeignKey('Book', models.DO_NOTHING)

    class Meta:
        managed = True
        db_table = 'author_book'
        unique_together = (('author', 'book'),)

    def __str__(self):
        return f'{self.author.name_field} - {self.book.name_field}'


class AvailableBooks(models.Model):
    shop = models.OneToOneField('Shop', models.DO_NOTHING, primary_key=True)  # The composite primary key (shop_id, book_id) found, that is not supported. The first column is selected.
    book = models.ForeignKey('Book', models.DO_NOTHING)
    stock_quantity = models.IntegerField()

    class Meta:
        managed = True
        db_table = 'available_books'
        unique_together = (('shop', 'book'),)

    def __str__(self):
        return f'{self.shop.adress} - {self.book.name_field}'


class Book(models.Model):
    book_id = models.AutoField(primary_key=True)
    name_field = models.CharField(db_column='name_', max_length=50)  # Field renamed because it ended with '_'.
    price_uah = models.IntegerField(db_column='price_UAH')  # Field name made lowercase.
    pages = models.IntegerField()

    class Meta:
        managed = True
        db_table = 'book'

    def __str__(self):
        return self.name_field


class BookGenre(models.Model):
    book = models.OneToOneField(Book, models.DO_NOTHING, primary_key=True)  # The composite primary key (book_id, genre_id) found, that is not supported. The first column is selected.
    genre = models.ForeignKey('Genre', models.DO_NOTHING)

    class Meta:
        managed = True
        db_table = 'book_genre'
        unique_together = (('book', 'genre'),)

    def __str__(self):
        return f'{self.book.name_field} - {self.genre.genre_name}'


class Feedback(models.Model):
    feedback_id = models.AutoField(primary_key=True)
    purchase = models.ForeignKey('Purchases', models.DO_NOTHING)
    feedback = models.CharField(max_length=200)
    rating = models.IntegerField()

    class Meta:
        managed = True 
        db_table = 'feedback'

    def __str__(self):
        return f'{self.purchase.reader.name_field} - {self.purchase.book.name_field}'

    


class Genre(models.Model):
    genre_id = models.AutoField(primary_key=True)
    genre_name = models.CharField(unique=True, max_length=50)

    class Meta:
        managed = True
        db_table = 'genre'

    def __str__(self):
        return self.genre_name


class Purchases(models.Model):
    purchase_id = models.AutoField(primary_key=True)
    reader = models.ForeignKey('Reader', models.DO_NOTHING)
    book = models.ForeignKey(Book, models.DO_NOTHING, blank=True, null=True)
    shop = models.ForeignKey('Shop', models.DO_NOTHING, blank=True, null=True)
    purchase_date = models.DateField()

    class Meta:
        managed = True
        db_table = 'purchases'
        unique_together = (('reader', 'book'),)

    def __str__(self):
        return f'{self.reader.name_field} - {self.book.name_field}'


class Reader(models.Model):
    reader_id = models.AutoField(primary_key=True)
    name_field = models.CharField(db_column='name_', max_length=20)  # Field renamed because it ended with '_'.
    surname = models.CharField(max_length=20)

    class Meta:
        managed = True
        db_table = 'reader'

    def __str__(self):
        return self.name_field


class Shop(models.Model):
    shop_id = models.IntegerField(primary_key=True)
    town = models.CharField(max_length=20)
    adress = models.CharField(unique=True, max_length=30)
    hotline = models.IntegerField(unique=True, blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'shop'

    def __str__(self):
        return self.adress