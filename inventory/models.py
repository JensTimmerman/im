from django.db import models


class Category(models.Model):
    """A category for a pantry item to be in
    e.g.
    UNCATEGORIZED
    GENRAL_STOCK  # bloem meel pasta
    CANS
    BREAKFAST
    SAVORIES
    SWEETS
    SNACKS
    SPICES
    DRINKS
    """
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name


class Unit(models.Model):
    """A unit
    e.g. Mililiter
    Grams
    Roll
    Tube
    Bag
    Bar
    Pack
    """
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name


class Location(models.Model):
    """Location for a pantry item line"""
    name = models.CharField(max_length=200, null=True, blank=True)
    in_location = models.ForeignKey("self", on_delete=models.PROTECT, null=True, blank=True)

    def __str__(self):
        if self.in_location and self.in_location.id != self.id:
            return self.name + ' ' + str(self.in_location)
        return self.name


class PantryItem(models.Model):
    """A think you keep in your pantry """
    category = models.ForeignKey(Category, on_delete=models.PROTECT)
    min_quantity = models.IntegerField(default=1) #, decimal_places=3, max_digits=32)
    # some things don't have a fixed expiry date, like legumes or garlic, we can specify a default expiration for
    # this.
    # if expiry duration is set the expiration date for a pantryitemline will be set to now + duration on save
    # represents days
    expiry_duration = models.IntegerField(null=True, blank=True)
    name =  models.CharField(max_length=200)
    unit = models.ForeignKey(Unit, on_delete=models.PROTECT, null=True)
    info = models.CharField(max_length=200, null=True, blank=True)
    # location is saved on a per item base, not itemline
    # you can have multiple pantries with subpantries
    location = models.ForeignKey(Location, on_delete=models.PROTECT, null=True, blank=True)

    def __str__(self):
        return self.name


class ShoppingListItem(PantryItem):
    """Items to buy now that aren't meant for the pantry but for imidiate usage"""
    pass


class PantryItemLine(models.Model):
    # user?
    pantry_item = models.ForeignKey(PantryItem, on_delete=models.PROTECT)
    quantity = models.IntegerField(default=1)
    expiry_date = models.DateField(null=True, blank=True)
    size = models.IntegerField(default=1) #, decimal_places=3, max_digits=32)
    info = models.CharField(max_length=200, null=True, blank=True)

    def unit(self):
        return self.pantry_item.unit

    def get_absolute_url(self):
        return reverse('pantryitemlinedetail', kwargs={'pk': self.pk})

    def __str__(self):
        return ' '.join([str(x) for x in [self.pantry_item.name,  self.quantity, 'X', self.size, self.pantry_item.unit]])

