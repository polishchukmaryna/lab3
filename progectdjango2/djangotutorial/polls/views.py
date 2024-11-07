from django.shortcuts import render

# Create your views here.
# from rest_framework.decorators import api_view
# from rest_framework.response import Response

from django.http import HttpResponse

# @api_view(['GET'])

def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")


from rest_framework import viewsets, permissions
from .models import Author, Book, Feedback, Purchases, Reader, Shop
from .serializers import AuthorSerializer, BookSerializer, FeedbackSerializer, PurchasesSerializer, ReaderSerializer, ShopSerializer

# from rest_framework.authentication import SessionAuthentication, BasicAuthentication, TokenAuthentication
# from rest_framework.permissions import IsAuthenticated

class AuthorViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows authors to be viewed or edited.
    """
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer
    permission_classes = [permissions.IsAuthenticated]
    # authentication_classes = [SessionAuthentication, BasicAuthentication, TokenAuthentication]
    # permission_classes = [IsAuthenticated]


class BookViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows books to be viewed or edited.
    """
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [permissions.IsAuthenticated]
    # authentication_classes = [SessionAuthentication, BasicAuthentication, TokenAuthentication]
    # permission_classes = [IsAuthenticated]


class FeedbackViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows feedback to be viewed or edited.
    """
    queryset = Feedback.objects.all()
    serializer_class = FeedbackSerializer
    permission_classes = [permissions.IsAuthenticated]
    # authentication_classes = [SessionAuthentication, BasicAuthentication, TokenAuthentication]
    # permission_classes = [IsAuthenticated]


class PurchasesViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows purchases to be viewed or edited.
    """
    queryset = Purchases.objects.all()
    serializer_class = PurchasesSerializer
    permission_classes = [permissions.IsAuthenticated]
    # authentication_classes = [SessionAuthentication, BasicAuthentication, TokenAuthentication]
    # permission_classes = [IsAuthenticated]


class ReaderViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows readers to be viewed or edited.
    """
    queryset = Reader.objects.all()
    serializer_class = ReaderSerializer
    permission_classes = [permissions.IsAuthenticated]
    # authentication_classes = [SessionAuthentication, BasicAuthentication, TokenAuthentication]
    # permission_classes = [IsAuthenticated]


class ShopViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows shops to be viewed or edited.
    """
    queryset = Shop.objects.all()
    serializer_class = ShopSerializer
    permission_classes = [permissions.IsAuthenticated]
    # authentication_classes = [SessionAuthentication, BasicAuthentication, TokenAuthentication]
    # permission_classes = [IsAuthenticated]