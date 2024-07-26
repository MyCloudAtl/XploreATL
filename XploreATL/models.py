from django.db import models

class Location(models.Model):
    county = models.CharField(max_length=255)
    state = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.county}, {self.state}"

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
    operations_hours = models.TextField(blank=True, null=True)
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
    operations_hours = models.TextField(blank=True, null=True)
    price_range = models.CharField(max_length=10, choices=[('$-$$', 'Low to Medium'), ('$$-$$$', 'Medium to High'), ('$$$-$$$$', 'High End')], blank=True)
    description = models.TextField(blank=True, default= 'no description')

    def __str__(self):
        return self.name
    
class Rating(models.Model):
    RATING_CHOICES = [(1, '1 Star'), (2, '2 Stars'), (3, '3 Stars'), (4, '4 Stars'), (5, '5 Stars')]
    rating = models.IntegerField(choices=RATING_CHOICES)
    date_posted = models.DateTimeField(auto_now_add=True)
    eatery = models.ForeignKey(Eatery, on_delete=models.CASCADE, related_name='reviews', null=True, blank=True)
    hotspot = models.ForeignKey(Hotspot, on_delete=models.CASCADE, related_name='reviews', null=True, blank=True)
    
    def __str__(self):
        return f"{self.rating} Stars - {self.eatery or self.hotspot}"
    
class CustomUser(models.Model):
    username = models.CharField(max_length=255)
    password = models.CharField(max_length=255)
    email = models.EmailField(max_length=254, unique=True, null=False, blank=False)

    def __str__(self):
        return self.username

class Profile(models.Model):
    customuser = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name='profiles', null=True)
    favorite_eateries = models.ManyToManyField(Eatery, blank=True, related_name='favorited_by')
    favorite_hotspots = models.ManyToManyField(Hotspot, blank=True, related_name='favorited_by')
    bookmarked_hotspots = models.ManyToManyField(Hotspot, blank=True, related_name='bookmarked_by')
    bookmarked_eateries = models.ManyToManyField(Eatery, blank=True, related_name='bookmarked_by')

    def __str__(self):
        return self.customuser.username

