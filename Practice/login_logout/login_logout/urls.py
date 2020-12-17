from django.contrib import admin
from django.urls import path
from django.contrib.auth import views as auth_views
# from django.contrib.auth.views import login_view
# from customer.views import login_view, signup_view
from customer import views
urlpatterns = [
    path('admin/', admin.site.urls),
    # path("login/", views.login_view, name= "login"),
    path('', views.home_view, name= "home"),
    path("signup/", views.signup_view, name = "signup"),
    path('login/', auth_views.LoginView.as_view(), name= "login"),
    
    path("customer/", views.cust_view, name="index"),
]
