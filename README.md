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
- shopping list based on min quantity

- one off shoping list

- easy clearing of shopping list
- correct capilisation

## low
- add recepies
- shopping list created based on recepy ingredients
- auto proposal of recepy based on next expiry dates
