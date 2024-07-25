from django.contrib import admin
from .models import Profile, Hotspot, Eatery, Location, User

admin.site.register(Location)
admin.site.register(Profile)
admin.site.register(Hotspot)
admin.site.register(Eatery)
admin.site.register(User)