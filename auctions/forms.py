from django import forms
from django.forms import ModelForm
from .models import *

# Get categories from admin as objects and turn into list
categories = Category.objects.all().values_list('name', 'name')
categories_list =[]

for category_object in categories:
    categories_list.append(category_object)


class ListingForm(ModelForm):
    class Meta:
        model = Listing
        fields = ('title', 'description', 'starting_bid', 'photo_url') 
        widgets = {
            'category' : forms.Select(choices = categories_list)
        }

class CommentForm(ModelForm):
    class Meta:
        model = Comment
        fields = ('body',)
        labels = {"body" : "" }

class BidForm(ModelForm):
    class Meta:
        model = Bid
        fields = ('new_bid',)
        labels = {'new_bid' : 'Place your bid'}
