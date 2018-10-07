# im
Pantry inventory management

# Inventory management system written in django - python
The object of this django app is to keep track of which goods you own, when they will expire, when you should consume them and when you shoud buy more.

## features
- Enter items in your pantry (or other locations, with their location) with their expiry date
- Items can have a minimum quantity you always want to keep in the pantry
 - a shopping list is automatically populated with items whose quantity is below this minimum quantity
- You get an overview of items per expiry date so you know what to consume first (or throw away)

- Extensive search and filtering and grouping on locations, categories, units, expiry date using the auto generated django admin
  interface
- Locations are recursive so things can be in the kitchen pantry closet on the 3rd shelf on the right and still be in
  the kitchen

# Getting started
`pip3 install django`


1. Add "inventory" to your INSTALLED_APPS setting like this::

    INSTALLED_APPS = [
        ...
        'inventory',
    ]

2. Include the inventory URLconf in your project urls.py like this::

    path('inventory/', include('inventory.urls')),

3. Run `python manage.py migrate` to create the polls models.

4. Start the development server and visit http://127.0.0.1:8000/admin/
   to create a pantry inventory (you'll need the Admin app enabled).

5. Visit http://127.0.0.1:8000/inventory/ to view your inventory website.

# feature requests
## High
- make expirations a calendar view, generate ics file to import
- public wishlist
- one off shoping list
- easy clearing of shopping list
- add easy consume view
 - save date consumed in history

# medium high
- mobile app
 - (requires rest api?)

# medium
- make work offline
- add users
 - federated? use sqrl instead of passwords?

# medium low
- allow for lending stuff out
 - auto mailings when things should be returned?
 - double bookkeeping of where things are if both parties have this set up
  - ipfs (+ blockchain?)
   - will be done in a seperate app, oos for inventory

- make it look something like this https://getbootstrap.com/docs/4.0/examples/dashboard/


- figure out average usage of items over time and predict how much to buy in shopping list based on average expiry
  dates
- figure out how long a certain item can last given current stock and average usage

- easily deploy somewhere (docker? on synology?)

## low
- add recepies
- shopping list created based on recepy ingredients
- auto proposal of recepy based on next expiry dates
- offer to buy things that have been on shopping list for a while online (in bulk/aggregated)
