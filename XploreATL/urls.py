from django.urls import path
from . import views
from rest_framework.routers import DefaultRouter

urlpatterns = [
    path('eateries/', views.EateryList.as_view(), name='eatery_list'),
    path('eateries/<int:pk>', views.EateryDetail.as_view(), name='eatery_detail'),
    path('hotspots/', views.HotspotList.as_view(), name="hotspot_list"),
    path('hotspots/<int:pk>', views.HotspotDetail.as_view(), name="hotspot_detail"),
    path('locations/', views.LocationList.as_view(), name="location_list"),
    path('locations/<int:pk>', views.LocationDetail.as_view(), name="location_detail"),
    path('ratings/', views.RatingList.as_view(), name="rating_list"),
    path('ratings/<int:pk>', views.RatingDetail.as_view(), name="rating_detail"),
    path('users/', views.UserList.as_view(), name="user_list"),
    path('users/<int:pk>', views.UserDetail.as_view(), name="user_detail"),
]