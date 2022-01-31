"""vivah URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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
from django.urls import path
from vivahapp import views as vivah_views
from twofa import views as twofa_views
from phone_verification import views as verify_views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', vivah_views.home, name="home"),
    path('verification/', verify_views.phone_verification, name='phone_verification'),  # noqa: E501
    path('verification/token/', verify_views.token_validation, name='token_validation'),  # noqa: E501
    path('verified/', verify_views.verified, name='verified'),
    path('2fa/', twofa_views.twofa, name='2fa'),
    path('token/sms', twofa_views.token_sms, name='token-sms'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
]
