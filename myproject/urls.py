"""
URL configuration for myproject project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.contrib import admin
from django.urls import include, path
from . import views

from rest_framework import routers
from tutorial.quickstart import views

router = routers.DefaultRouter()
router.register(r'authors', views.AuthorViewSet)
router.register(r'books', views.BookViewSet)
router.register(r'feedbacks', views.FeedbackViewSet)
router.register(r'genres', views.GenreViewSet)
router.register(r'purchasess', views.PurchasesViewSet)
router.register(r'readers', views.ReaderViewSet)
router.register(r'shops', views.ShopViewSet)
router.register(r'authorBooks', views.AuthorBookViewSet)
router.register(r' availableBookss', views.AvailableBooksViewSet)
router.register(r'bookGenres', views.BookGenreViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]

urlpatterns = [
    path("admin/", admin.site.urls),
    #path("libraryapp/", include("libraryapp.urls")),
    path("", views.index, name="index"),
]
