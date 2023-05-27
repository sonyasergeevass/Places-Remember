"""
URL configuration for places_remember project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
from django.contrib.auth.views import LogoutView
from app_pr import views

urlpatterns = [
    # path('', views.login_page_vk, name='login_page_vk'),
    path('', views.login_page_vk, name='login_vk'),
    path('home/', views.home_page, name='home'),
    # path('logout/', views.logout_view, name='logout'),
    path('logout/', LogoutView.as_view(next_page='login_vk'),
         name='logout'),
    path('admin/', admin.site.urls),
    path('accounts/', include('allauth.urls')),
]
