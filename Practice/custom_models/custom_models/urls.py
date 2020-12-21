from django.contrib import admin
from django.urls import path
from custom_app import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name= "index"),
    path('signup/', views.signup, name= "signup"),
    path('login/', auth_views.LoginView.as_view(), name= "login"),
    path('home/', views.home, name= 'home')
]
