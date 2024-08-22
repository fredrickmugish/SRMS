from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name="index"),
    path('register/', views.register, name="register"),
    path('user_panel/', views.user_panel, name="user_panel"),
    path('logout/', views.logout_user, name="logout"),
   
]
