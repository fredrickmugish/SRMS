from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.index, name="index"),
    path('login_user/', views.login_user, name="login_user"),
    path('register/', views.register, name="register"),
    path('user_panel/', views.user_panel, name="user_panel"),
    path('logout/', views.logout_user, name="logout"),
    path('dashboard/', views.dashboard, name="dashboard"),
    path('registration/', views.registration, name="registration"),
    path('registration/add', views.registrationAdd, name="registrationAdd"),
    path('about/', views.about, name="about"),
    path('site_courses/', views.site_courses, name="site_courses"),
    path('contact/', views.contact, name="contact"),
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

