# UVA Craigslist Clone # 
This was a group project at UVA for CS3240 - Advanced Software Development. 
To start, here is the link to the app, deployed on Heroku: https://loxodante.herokuapp.com

## Login and Home ##
This link lands a user on a login page - this page briefly explains what the site is for and asks the user to login with netbadge.
Once the user has gone through the login process, they reach the home page. It is our intention for this page first to clear up for a user any possible ambiguity on the basics of the site that may have existed at login, and then to direct them on how they might use the site themselves. 
The two basic options are to either look for items to buy, or post items to sell. 
If the user intends to buy something, some common categories are listed on the home page with links that will take the user to the listing page for that category.
If they user intends to sell something, there is a direct link in the navbar to the page where they can create a listing on the site.

## Listings ##
If they choose to visit the already existing posts, they are landed on a page that has filters for several common types of items: Textbooks, Furniture, Clothes, and Electronics. If an item has been listed as "other", there is a filter for this category as well. By default, when a user first lands on this page, all existing listings are shown.

The user can either filter by these categories listed above, or they can search for a more specific item using the search engine at the top of the page. This search engine searches for strings that are included in both the title of an item or its description.

Each individual post lists a title, picture, and other information about the post. The user can simply click on the seller's computing ID to open up their default email client to send a message.

The user can also view the post's pickup location by clicking the "View pickup location" button. This will open up a new page that displays a google map with a pin on the location where the seller chose to have the item picked up.

## Create New Listing ##
If the user chooses to create a listing for an item they wish to sell, the can go the page labeled "Create New Listing"
Once on this page, there are some brief guidelines for making listings, then a form the users can fill out with various pieces of information.

Once the user has created their post, they can click on "Create" which redirects them to the "Listings" page where their listing, along with all other listings will appear. This is the same page that users will land on when they click on the "Listings" link in the navbar.

For the "pickup location" input field, the user can input any address, and our Google Maps plugin will find the closest match to their input.


## Profile ##
If a user wishes to view their profile information or their posts, they can visit the "Profile" link in the navbar. There are three main sections to the profile page. The first is just the user's information - all of this information is collected from Google, so it is not possible to edit the information. 

The next section is a user's "Active Posts". This is the set of all posts that a user has made that they have not yet sold, and are therefore currently listed on the site where other users can view them. Finally, there is a section that consists only of posts that a user has sold or "archived". The user can take a post in their active listings and mark it as sold, which takes that listing off the public listings page and adds it to the archived posts. If a user for some reason needs to re-list a post they had previously marked as sold, they can do so on their profile by visiting their archived posts and then clicking the button "Re-publish Listing" on the post they wish to re-list. Also, if a user decides that they do not wish to keep a certain post in their archive, they can delete it altogether using the "Delete this Listing" button on an archived listing.


This covers all the basic functionalities of the site.
