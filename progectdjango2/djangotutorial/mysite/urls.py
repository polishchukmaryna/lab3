"""
URL configuration for mysite project.

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
from rest_framework import routers
from polls import views
# from djangotutorial.polls import views

# from rest_framework.authtoken import views as drf_views

router = routers.DefaultRouter()
router.register(r'authors', views.AuthorViewSet)
router.register(r'books', views.BookViewSet)
router.register(r'feedbacks', views.FeedbackViewSet)
router.register(r'purchases', views.PurchasesViewSet)
router.register(r'readers', views.ReaderViewSet)
router.register(r'shops', views.ShopViewSet)

# Register all endpoints of the site here
# реєструємо все до чого ми можемо доступатися
urlpatterns = [
    path("polls/", include("polls.urls")), # View routes
    path("admin/", admin.site.urls), 
    path('api/', include(router.urls)), # API Routes
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),

    # path('api-token-auth/', drf_views.obtain_auth_token),  # Endpoint для отримання токену
]
