from django.urls import path, include
from django.contrib import admin
from XploreATL import views
from rest_framework.routers import DefaultRouter


from django.conf.urls import include


urlpatterns = [
    path('admin/', admin.site.urls,),
    path('', include('XploreATL.urls')),
    path('api-auth', include('rest_framework.urls', namespace='rest_framework'))
    ]