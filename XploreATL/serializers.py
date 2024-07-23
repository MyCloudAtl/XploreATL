from rest_framework import serializers
from .models import Eatery, Hotspot, Profile, Location

class EaterySerializer(serializers.HyperlinkedModelSerializer):
    location = serializers.HyperlinkedRelatedField(
        view_name='location_detail',
        read_only=True
    )
    location_id = serializers.PrimaryKeyRelatedField(
        queryset=Location.objects.all(),
        source='location'
    )
    class Meta:
        model = Eatery
        fields = '__all__'

class HotspotSerializer(serializers.HyperlinkedModelSerializer):
    location = serializers.HyperlinkedRelatedField(
        view_name='location_detail',
        read_only=True
    )
    location_id = serializers.PrimaryKeyRelatedField(
        queryset=Location.objects.all(),
        source='location'
    )
    class Meta:
        model = Hotspot
        fields = '__all__'

class ProfileSerializer(serializers.HyperlinkedModelSerializer):
    # user = UserSerializer()
    favorite_eateries = EaterySerializer(many=True, read_only=True)
    favorite_hotspots = HotspotSerializer(many=True, read_only=True)
    bookmarked_eateries = EaterySerializer(many=True, read_only=True)
    bookmarked_hotspots = HotspotSerializer(many=True, read_only=True)
    class Meta:
        model = Profile
        fields = ['favorite_eateries', 'favorite_hotspots', 'bookmarked_eateries', 'bookmarked_hotspots']

class LocationSerializer(serializers.HyperlinkedModelSerializer):
    eatery = EaterySerializer(
        many=True,
        read_only=True
    )
    hotspot = HotspotSerializer(
        many=True,
        read_only=True
    )
    class Meta:
        model = Location
        fields = ['id', 'name', 'county', 'city', 'state']
