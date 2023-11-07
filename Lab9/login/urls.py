from django.urls import path
from . import views

urlpatterns = [
    path('', views.loginPage, name='login'),
    path('register', views.registerPage, name='register'),
    path('me', views.me, name='me'),
    path('logout', views.doLogout, name='logout')
]