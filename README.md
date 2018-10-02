# im
Pantry inventory management

# Inventory management system written in django - python
The object of this django app is to keep track of which goods you own, when they will expire, when you should consume them and when you shoud buy more.

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
- add locations to items
- public wishlist
- one off shoping list
- add easy consume view
 - save date consumed in history

## medium
- make it look something like this https://getbootstrap.com/docs/4.0/examples/dashboard/

- easy clearing of shopping list

## low
- add recepies
- shopping list created based on recepy ingredients
- auto proposal of recepy based on next expiry dates
