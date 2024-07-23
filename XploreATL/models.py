from django.db import models

class Location(models.Model):
    county = models.CharField(max_length=255)
    state = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Eatery(models.Model):
    location = models.ForeignKey(Location, on_delete=models.CASCADE, related_name='eateries')
    image = models.URLField(max_length=500, null=True)
    category = models.CharField(max_length=100, choices=[('restaurant', 'Restaurant'),('cafe', 'Cafe'),('bakery', 'Bakery'),])
    name = models.CharField(max_length=255)
    address = models.CharField(max_length=255)
    city = models.CharField(max_length=100)
    state = models.CharField(max_length=100)
    zip_code = models.CharField(max_length=20)
    cuisine = models.CharField(max_length=255, blank=True)
    phone_number = models.CharField(max_length=20, blank=True)
    website = models.URLField(blank=True)
    opening_time = models.TimeField(blank=True, null=True)
    closing_time = models.TimeField(blank=True, null=True)
    price_range = models.CharField(max_length=10, choices=[('$-$$', 'Low to Medium'), ('$$-$$$', 'Medium to High'), ('$$$-$$$$', 'High End')], blank=True)
    description = models.TextField(blank=True, default= 'no description')

    def __str__(self):
        return self.name

class Hotspot(models.Model):
    location = models.ForeignKey(Location, on_delete=models.CASCADE, related_name='hotspots')
    image = models.URLField(max_length=500, null=True)
    category = models.CharField(max_length=100, choices=[('daytime', 'Daytime'), ('nightlife', 'Nightlife')])
    name = models.CharField(max_length=255)
    address = models.CharField(max_length=255)
    city = models.CharField(max_length=100)
    state = models.CharField(max_length=100)
    zip_code = models.CharField(max_length=20)
    phone_number = models.CharField(max_length=20, blank=True)
    website = models.URLField(blank=True)
    opening_time = models.TimeField(blank=True, null=True)
    closing_time = models.TimeField(blank=True, null=True)
    price_range = models.CharField(max_length=10, choices=[('$-$$', 'Low to Medium'), ('$$-$$$', 'Medium to High'), ('$$$-$$$$', 'High End')], blank=True)
    description = models.TextField(blank=True, default= 'no description')

    def __str__(self):
        return self.name

class Profile(models.Model):
    # user = models.OneToOneField(User, on_delete=models.CASCADE)
    favorite_eateries = models.ManyToManyField(Eatery, blank=True, related_name='favorited_by')
    favorite_hotspots = models.ManyToManyField(Hotspot, blank=True, related_name='favorited_by')
    bookmarked_hotspots = models.ManyToManyField(Hotspot, blank=True, related_name='bookmarked_by')
    bookmarked_eateries = models.ManyToManyField(Eatery, blank=True, related_name='bookmarked_by')

    def __str__(self):
        return self.user.username

