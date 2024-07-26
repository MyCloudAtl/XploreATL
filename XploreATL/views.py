from django.shortcuts import render
from rest_framework import generics
from .serializers import EaterySerializer, HotspotSerializer, ProfileSerializer, LocationSerializer, UserSerializer, RatingSerializer
from .models import Eatery, Hotspot, Location, Profile, User, Rating
from django.contrib.auth.models import User
from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view

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

@api_view(['POST'])
def user_list(request):
    # print (request.data)
    if request.method == 'POST': 
        serializer = UserSerializer(User, data=request.data)
        if serializer.is_valid():
            serializer.save()
        #     return Response(serializer.data)
        # return Response(serializer.errors)
            return Response({'message': 'User created successfully!'}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class UserDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

    
def profile(request):
    return render(request, 'profile.html')
