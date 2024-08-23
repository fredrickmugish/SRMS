from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name="index"),
    path('login_user/', views.login_user, name="login_user"),
    path('register/', views.register, name="register"),
    path('user_panel/', views.user_panel, name="user_panel"),
    path('logout/', views.logout_user, name="logout"),
    path('dashboard/', views.dashboard, name="dashboard"),
    path('registration/', views.registration, name="registration"),
]
