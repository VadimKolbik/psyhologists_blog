from django.urls import path, include
from django.contrib.flatpages import views

app_name = 'flatpage_main'

urlpatterns = [
    path('about-me/', views.flatpage, {'url': '/about-me/'}, name='about_me'),
    path('contacts/', views.flatpage, {'url': '/contacts/'}, name='contacts'),
]

