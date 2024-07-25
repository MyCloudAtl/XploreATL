from rest_framework import serializers
from django.db.models import Avg
from .models import Eatery, Hotspot, Profile, Location, User, Rating

class EaterySerializer(serializers.HyperlinkedModelSerializer):
    location = serializers.HyperlinkedRelatedField(
        view_name='location_detail',
        read_only=True
    )
    location_id = serializers.PrimaryKeyRelatedField(
        queryset=Location.objects.all(),
        source='location'
    )
    avg_rating = serializers.SerializerMethodField()

    class Meta:
        model = Eatery
        fields = ('location','location_id','image','category','name','address','city','state','zip_code','cuisine','phone_number','website','operations_hours','price_range','description','avg_rating')

    def get_avg_rating(self, obj):
        avg_rating = obj.reviews.aggregate(Avg('rating'))['rating__avg']
        return round(avg_rating, 2) if avg_rating else 'No ratings yet'
    
class HotspotSerializer(serializers.HyperlinkedModelSerializer):
    location = serializers.HyperlinkedRelatedField(
        view_name='location_detail',
        read_only=True
    )
    location_id = serializers.PrimaryKeyRelatedField(
        queryset=Location.objects.all(),
        source='location'
    )
    avg_rating = serializers.SerializerMethodField()

    class Meta:
        model = Hotspot
        fields = ('location','location_id','image','category','name','address','city','state','zip_code','phone_number','website','operations_hours','price_range','description','avg_rating')

    def get_avg_rating(self, obj):
        avg_rating = obj.reviews.aggregate(Avg('rating'))['rating__avg']
        return round(avg_rating, 2) if avg_rating else 'No ratings yet'
    
class ProfileSerializer(serializers.HyperlinkedModelSerializer):
    user = serializers.PrimaryKeyRelatedField(queryset=User.objects.all())
    favorite_eateries = EaterySerializer(many=True, read_only=True)
    favorite_hotspots = HotspotSerializer(many=True, read_only=True)
    bookmarked_eateries = EaterySerializer(many=True, read_only=True)
    bookmarked_hotspots = HotspotSerializer(many=True, read_only=True)
    class Meta:
        model = Profile
        fields = ['user','favorite_eateries', 'favorite_hotspots', 'bookmarked_eateries', 'bookmarked_hotspots']

class RatingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Rating
        fields = ('rating', 'date_posted', 'eatery', 'hotspot')

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