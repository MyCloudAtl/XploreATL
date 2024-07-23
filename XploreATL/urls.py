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
    path('profiles/', views.ProfileList.as_view(), name="profile_list"),
    path('profiles/<int:pk>', views.ProfileDetail.as_view(), name="profile_detail"),
]