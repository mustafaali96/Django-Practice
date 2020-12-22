from django.contrib import admin
from django.urls import path
from custom_app import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index_view, name= "index"),
    path('signup/', views.signup_view, name= "signup"),
    path('login/', auth_views.LoginView.as_view(), name= "login"),
    path('home/', views.home_view, name= 'home'),
    path('logout/', auth_views.LogoutView.as_view(), name= 'logout')
]
