"""
URL configuration for teretana_aplikacija project.

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
from django.urls import path
from django.contrib.auth import views as auth_views
from teretana import views
from teretana.views import GenericListView, GenericDetailView, GenericCreateView, GenericUpdateView, GenericDeleteView


urlpatterns = [
    path('admin/', admin.site.urls),
    path('login/', auth_views.LoginView.as_view(template_name='login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('register/', views.register, name='register'),
    path('admin-dashboard/', views.admin_dashboard, name='admin_dashboard'),
    path('', views.home, name='home'),
    path('user-home/', views.user_home, name='user_home'),
    path('<str:model>/', GenericListView.as_view(), name='generic_list'),
    path('<str:model>/<int:pk>/', GenericDetailView.as_view(), name='generic_detail'),
    path('<str:model>/add/', GenericCreateView.as_view(), name='generic_create'),
    path('<str:model>/<int:pk>/edit/', GenericUpdateView.as_view(), name='generic_update'),
    path('<str:model>/<int:pk>/delete/', GenericDeleteView.as_view(), name='generic_delete'),
]