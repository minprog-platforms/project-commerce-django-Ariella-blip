from django.urls import path

from . import views

urlpatterns = [
    #path("", views.index, name="index"),
    path("", views.Index.as_view(), name="index"),
    path('listing/<int:pk>', views.ListingPage.as_view(), name = 'listing-page'),
    # path("listing/<int:listing_id>/bid/", views.Bidding.as_view(), name ='add-bid'),
    path("listing/<int:listing_id>/delete/", views.close_listing, name="close-listing"),
    path("listing/<int:listing_id>/watchlist/", views.add_to_watchlist, name="add-watchlist"),
    path("listing/<int:listing_id>/bid/", views.add_bid, name="add-bid"),
    path("listing/<int:listing_id>/comment/", views.add_comment, name="add-comment"),
    path("login", views.login_view, name="login"),
    path("logout", views.logout_view, name="logout"),
    path("register", views.register, name="register"),
    path("create_listing", views.create_listing, name='listing')
]