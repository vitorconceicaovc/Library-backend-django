"""
URL configuration for locallibrary project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
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
from django.urls import path, include
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
    TokenVerifyView
)
from django.conf import settings
from django.conf.urls.static import static
from django.views.generic import RedirectView
from . import views
from .views import user_list, user_detail

urlpatterns = [
    path('admin/', admin.site.urls),
]

# Use include() to add paths from the catalog application
urlpatterns += [
    path('catalog/', include('catalog.urls')),
]

# Add URL maps to redirect the base URL to our application
urlpatterns += [
    path('', RedirectView.as_view(url='catalog/', permanent=True)),
]

# Use static() to add URL mapping to serve static files during development (only)

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

urlpatterns += [
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('api/token/verify/', TokenVerifyView.as_view(), name='token_verify'),
     path('api/rest_self_user/', views.REST_self_user.as_view()),

    path('api/register/', views.register_user, name='register_user'),
    path('api/user/<int:pk>/', views.user_detail, name='user_detail'),
    path('api/users/', views.user_list, name='user_list'),
]