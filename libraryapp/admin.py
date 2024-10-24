from django.contrib import admin

# Register your models here.
from .models import Author, Book, Feedback, Genre, Purchases, Reader, Shop, AuthorBook, AvailableBooks, BookGenre
admin.site.register (Author)
admin.site.register (Book)
admin.site.register (Feedback)
admin.site.register (Genre)
admin.site.register (Purchases)
admin.site.register (Reader)
admin.site.register (Shop)
admin.site.register (AuthorBook)
admin.site.register (AvailableBooks)
admin.site.register (BookGenre)