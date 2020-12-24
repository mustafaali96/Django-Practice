from django.contrib import admin
from django.urls import path
from custom_app import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('admin/', admin.site.urls, name = "admin"),
    path('', views.index_view, name= "index"),
    path('signup/', views.signup_view, name= "signup"),
    path('login/', auth_views.LoginView.as_view(), name= "login"),
    path('profile/', views.home_view, name= 'home'),
    path('logout/', auth_views.LogoutView.as_view(), name= 'logout'),
    path('profile/update/', views.update_record, name= 'update'),
    path('students/', views.record_list, name= "studentRec"),
    path('teachers/', views.record_list, name= "teachersRec"),
    path('records/', views.record_list, name= "allRec"),
    # path('Student<id>/', views.studentsRec_view, name= "student_id_rec"),
]
