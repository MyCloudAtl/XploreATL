from django.shortcuts import render
from rest_framework import generics
from .serializers import EaterySerializer, HotspotSerializer, ProfileSerializer, LocationSerializer, UserSerializer, RatingSerializer
from .models import Eatery, Hotspot, Location, Profile, User, Rating

class EateryList(generics.ListCreateAPIView):
    queryset = Eatery.objects.all()
    serializer_class = EaterySerializer

class EateryDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Eatery.objects.all()
    serializer_class = EaterySerializer

class HotspotList(generics.ListCreateAPIView):
    queryset = Hotspot.objects.all()
    serializer_class = HotspotSerializer

class HotspotDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Hotspot.objects.all()
    serializer_class = HotspotSerializer

class LocationList(generics.ListCreateAPIView):
    queryset = Location.objects.all()
    serializer_class = LocationSerializer

class LocationDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Location.objects.all()
    serializer_class = LocationSerializer

class ProfileList(generics.ListCreateAPIView):
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer

class ProfileDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer

class RatingList(generics.ListCreateAPIView):
    queryset = Rating.objects.all()
    serializer_class = RatingSerializer

class RatingDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Rating.objects.all()
    serializer_class = RatingSerializer

class UserList(generics.ListCreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class UserDetail(generics.ListCreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer


def profile(request):
    return render(request, 'profile.html')
