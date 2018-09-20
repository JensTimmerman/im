from django.db import models

# Create your models here.

CATEGORIES = (
    ('UC', 'UNCATEGORIZED'),  # bloem meel pasta
    ('GS', 'GENRAL_STOCK'),  # bloem meel pasta
    ('CANS', 'CANS'),
    ('BR', 'BREAKFAST'),
    ('SAV', 'SAVORIES'),
    ('SW', 'SWEETS'),
    ('SN', 'SNACKS'),
    ('SP', 'SPICES'),
    ('DR', 'DRINKS'),
)

UNITS = (
    ('L', 'miliLiter'),
    ('GR', 'Grams'),
    ('Roll', 'Roll'),
    ('Tube', 'Tube'),
    ('Bag', 'Bag'),
    ('Bar', 'Bar'),
    ('Pack', 'Pack'),
)



#class ShoppingList(models.Model):
    # - pantryitems < min_quantity in pantryitemlists
    # - shoppinglistitems
    # - user ?
    # info
    # quantity
    # unit
    # name

class PantryItem(models.Model):
    # user?
    name =  models.CharField(max_length=200)
    category = models.CharField(max_length=200, choices=CATEGORIES)
    min_quantity = models.IntegerField(default=1) #, decimal_places=3, max_digits=32)
    unit = models.CharField(max_length=20, null=True, blank=True, choices=UNITS)
    info = models.CharField(max_length=200, null=True, blank=True)

    def __str__(self):
        return self.name

class PantryItemLine(models.Model):
    # user?
    pantry_item = models.ForeignKey(PantryItem, on_delete=models.PROTECT, default='UC' )
    quantity = models.IntegerField(default=1)
    expiry_date = models.DateField(null=True, blank=True)
    size = models.IntegerField(default=1) #, decimal_places=3, max_digits=32)
    unit = models.CharField(max_length=20, null=True, blank=True, choices=UNITS)
    info = models.CharField(max_length=200, null=True, blank=True)

    def __str__(self):
        return self.pantry_item.name + ' ' + str(self.quantity)
