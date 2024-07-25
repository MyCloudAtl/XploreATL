from rest_framework import serializers
from .models import Eatery, Hotspot, Profile, Location, User

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
        fields = ('location','location_id','image','category','name','address','city','state','zip_code','cuisine','phone_number','website','operations_hours','price_range','description')

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
        fields = ('location','location_id','image','category','name','address','city','state','zip_code','phone_number','website','operations_hours','price_range','description')

class ProfileSerializer(serializers.HyperlinkedModelSerializer):
    user = serializers.PrimaryKeyRelatedField(queryset=User.objects.all())
    favorite_eateries = EaterySerializer(many=True, read_only=True)
    favorite_hotspots = HotspotSerializer(many=True, read_only=True)
    bookmarked_eateries = EaterySerializer(many=True, read_only=True)
    bookmarked_hotspots = HotspotSerializer(many=True, read_only=True)
    class Meta:
        model = Profile
        fields = ['user','favorite_eateries', 'favorite_hotspots', 'bookmarked_eateries', 'bookmarked_hotspots']

class LocationSerializer(serializers.HyperlinkedModelSerializer):
    # eateries = serializers.PrimaryKeyRelatedField(many=True, read_only=True)
    # hotspots = serializers.PrimaryKeyRelatedField(many=True, read_only=True)
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
        fields = ['id', 'county', 'state']

class UserSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = Location
        fields = ('username')