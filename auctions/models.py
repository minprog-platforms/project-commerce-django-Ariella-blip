from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    pass


class Category(models.Model):
    name = models.CharField(max_length = 50)

    def __str__(self):
        return self.name


class Comment(models.Model):
    author = models.ForeignKey(User, related_name = "author", on_delete = models.CASCADE) 
    body = models.TextField(max_length = 1000, blank = True)
    date = models.DateTimeField(auto_now = True)
    
    def __str__(self):
        return 'Date: %s, User: %s' % (self.date, self.author) 


class Bid(models.Model):
    bidder = models.ForeignKey(User, related_name = "bidder", on_delete = models.CASCADE, null = True) 
    new_bid = models.PositiveIntegerField(default = 0)


class Listing(models.Model):
    title = models.CharField(max_length = 255)
    description = models.TextField(max_length = 1000) #max_length kan miss weg?
    starting_bid = models.DecimalField(decimal_places = 2, max_digits = 8) 
    photo_url = models.CharField(max_length = 255, default = "No photo available", blank = True) #null sets default value to zero, and blank allows this field not to be requiered
    category = models.CharField(max_length = 50, default = "None", blank = True)
    user = models.ForeignKey(User, related_name = "user_listing", on_delete = models.CASCADE, null = True) 
    comments = models.ManyToManyField(Comment, blank=True, related_name="comments")
    bids = models.ManyToManyField(Bid, blank=True, related_name="bids")

    def __str__(self):
        return self.title


class Watchlist(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    listings = models.ManyToManyField(Listing, blank=True)