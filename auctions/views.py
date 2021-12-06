from django.contrib.auth import authenticate, login, logout
from django.db import IntegrityError
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect
from django.urls import reverse
from django.views.generic import ListView, DetailView, CreateView

from .models import *
from .forms import *


class Index(ListView):
    model = Listing
    template_name = "auctions/index.html"


class ListingPage(DetailView):
    model = Listing 
    template_name = "auctions/listing.html"  
    

def login_view(request):
    if request.method == "POST":

        # Attempt to sign user in
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)

        # Check if authentication successful
        if user is not None:
            login(request, user)
            return HttpResponseRedirect(reverse("index"))
        else:
            return render(request, "auctions/login.html", {
                "message": "Invalid username and/or password."
            })
    else:
        return render(request, "auctions/login.html")


def logout_view(request):
    logout(request)
    return HttpResponseRedirect(reverse("index"))


def register(request):
    if request.method == "POST":
        username = request.POST["username"]
        email = request.POST["email"]

        # Ensure password matches confirmation
        password = request.POST["password"]
        confirmation = request.POST["confirmation"]
        if password != confirmation:
            return render(request, "auctions/register.html", {
                "message": "Passwords must match."
            })

        # Attempt to create new user
        try:
            user = User.objects.create_user(username, email, password)
            user.save()
        except IntegrityError:
            return render(request, "auctions/register.html", {
                "message": "Username already taken."
            })
        login(request, user)
        return HttpResponseRedirect(reverse("index"))
    else:
        return render(request, "auctions/register.html")


def create_listing(request):
    try:
        user = User.objects.get(username = request.user)
    except User.DoesNotExist:
        return render(request, "auctions/login.html")

    submitted = False
    if request.method == "POST":
        form = ListingForm(request.POST)
        if form.is_valid():
            listing = form.save(commit=False)
            listing.user = user
            form.save()
            submitted = True
            return render(request, "auctions/create_listing.html", {
                 "form" : form,
                 "submitted" : submitted
             })

    form = ListingForm()
    return render(request, "auctions/create_listing.html", {
                    "form" : form
                })


def close_listing(request, listing_id):
    query = Listing.objects.get(pk=listing_id)
    query.delete()
    return HttpResponseRedirect(reverse("index"))


def add_to_watchlist(request, listing_id):
    try:
        user = User.objects.get(username = request.user)
        print(user)
    except User.DoesNotExist:
        return render(request, "auctions/login.html")

    listing = Listing.objects.get(pk=listing_id)

    watchlist = Watchlist(user = user)
    watchlist.save()
    watchlist.listings.add(listing)

    return HttpResponseRedirect(reverse("index"))


def add_bid(request, listing_id):
    try:
        user = User.objects.get(username = request.user)
    except User.DoesNotExist:
        return render(request, "auctions/login.html")

    if request.method == 'POST':
        # if form.is_valid():   
        form = BidForm(request.POST)
        bid = form.save(commit=False)

        if 'go_back_button' in request.POST:
            return HttpResponseRedirect(reverse("listing-page", args=[listing_id]))

        if form.cleaned_data['new_bid'] < listing.starting_bid:
            return render(request, "auctions/add_bid.html", {
            "form" : form,
            "message" : "Your bid must be higher that the current offer!"
            })
    
        listing.starting_bid = form.cleaned_data['new_bid']
        bid.save()
        listing.bids.add(bid)
        listing.save()

        return render(request, "auctions/add_bid.html", {
        "form" : form
    })

    form = BidForm()
    return render(request, "auctions/add_bid.html", {
        "form" : form
    })


def add_comment(request, listing_id):
    listing = Listing.objects.get(pk=listing_id)
    submitted = False 
    error = False

    try:
        user = User.objects.get(username = request.user)
    except User.DoesNotExist:
        return render(request, "auctions/login.html")

    if 'go_back_button' in request.POST:
        return HttpResponseRedirect(reverse("listing-page", args=[listing_id]))

    if request.method == 'POST':   
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.author = user

            if not form.cleaned_data['body']:
                error = True 
                return render(request, "auctions/comment.html", {
                "error" : error,
                "form" : form
            })
            
            comment.save()
            listing.comments.add(comment)
            listing.save()
            submitted = True 

            return render(request, "auctions/comment.html", {
            "submitted" : submitted,
            "form" : form
        })

    form = CommentForm()
    return render(request, "auctions/comment.html", {
        "form" : form
    })
