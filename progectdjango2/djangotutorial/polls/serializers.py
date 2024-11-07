# from django.contrib.auth.models import Group, User
from rest_framework import serializers
from .models import Author, Book, Feedback, Purchases, Reader, Shop 

class AuthorSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Author
        fields = '__all__'

class BookSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Book
        fields = '__all__'

class FeedbackSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Feedback
        fields = '__all__'

class PurchasesSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Purchases
        fields = '__all__'


class ReaderSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Reader
        fields = '__all__'


class ShopSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Shop
        fields = '__all__'