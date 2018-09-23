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
    category = models.CharField(max_length=200, choices=CATEGORIES, default='UC')
    min_quantity = models.IntegerField(default=1) #, decimal_places=3, max_digits=32)
    unit = models.CharField(max_length=20, null=True, blank=True, choices=UNITS)
    info = models.CharField(max_length=200, null=True, blank=True)

    def __str__(self):
        return self.name

class PantryItemLine(models.Model):
    # user?
    pantry_item = models.ForeignKey(PantryItem, on_delete=models.PROTECT)
    quantity = models.IntegerField(default=1)
    expiry_date = models.DateField(null=True, blank=True)
    size = models.IntegerField(default=1) #, decimal_places=3, max_digits=32)
    unit = models.CharField(max_length=20, null=True, blank=True, choices=UNITS)
    info = models.CharField(max_length=200, null=True, blank=True)

    def get_absolute_url(self):
        return reverse('pantryitemlinedetail', kwargs={'pk': self.pk})

    def __str__(self):
        return ' '.join([str(x) for x in [self.pantry_item.name,  self.quantity, 'X', self.size, self.unit]])
