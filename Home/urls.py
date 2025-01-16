from django.contrib import admin
from django.urls import path, include
from Home import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name='index'),
    path('verify', views.verify, name='verify'),
    path('register', views.register, name='register')
]