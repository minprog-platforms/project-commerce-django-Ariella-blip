# Application "Auctions"

An application made for finding auction listings, creating listings, bidding on them, adding them on a watchlist, commenting on them and categorising them. 
For all of the above except for displaying auctions, a login is required. 


# Class diagrams: "models.py"
![Alt text](https://github.com/minprog-platforms/project-commerce-django-Ariella-blip/blob/main/Schetsen/commerce:models.py.png)

# Sketches
![alt text](https://github.com/minprog-platforms/project-commerce-django-Ariella-blip/blob/main/Schetsen/commerce:homepage.png)

layout.html:
When signed in the user will see "signed in as >username<". 
When not signed in the user will see "not signed in". 
Below that links are provided for the different pages. 

index.html:
all the listings are listed, links are provided to their listing page.

![alt text](https://github.com/minprog-platforms/project-commerce-django-Ariella-blip/blob/main/Schetsen/commerce:listing-page.png)

listing.html:
The listing is displayed with the current price.
If the user visiting the pages is the user signed in, than he/she can close the listing.
With the button "add to list" a user can add the listing to their watchlist.
With the button "bid" the user can bid to a bidding form (add_bid.html).
With the button "comment" the user can go to a comment form (comment.html).
Below is a section that displays all comments.

add_bid.html:
The user can bid on the item via form, if the entered price is higher than the current offer.

comment.html:
The user can add a comment to the listings page.

![alt text](https://github.com/minprog-platforms/project-commerce-django-Ariella-blip/blob/main/Schetsen/commerce:create-listing.png)

create listing.html:
The user can create a listing by populating the form and pressing the button "create".

![alt text](https://github.com/minprog-platforms/project-commerce-django-Ariella-blip/blob/main/Schetsen/commerce:find-category.png)

categories.html:
The user gets a list of all categories with links to their category pages.

![alt text](https://github.com/minprog-platforms/project-commerce-django-Ariella-blip/blob/main/Schetsen/commerce:find-category.png)

category.html:
When clicking on the category, the user is taken to a page where all the listings in that category are listed.

![alt text](https://github.com/minprog-platforms/project-commerce-django-Ariella-blip/blob/main/Schetsen/commerce:my-watchlist.png)

watchlist.html:
After clicking on "my watchlist" in the menu bar the user is taken to a page where all their watchlist listings are displayed with links to their corresponding pages.

