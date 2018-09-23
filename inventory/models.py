from django.db import models

# Create your models here.


UNITS = (
    ('L', 'miliLiter'),
    ('GR', 'Grams'),
    ('Roll', 'Roll'),
    ('Tube', 'Tube'),
    ('Bag', 'Bag'),
    ('Bar', 'Bar'),
    ('Pack', 'Pack'),
)


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

class PantryItem(models.Model):
    # user?
    name =  models.CharField(max_length=200)
    category = models.ForeignKey(Category, on_delete=models.PROTECT)
    min_quantity = models.IntegerField(default=1) #, decimal_places=3, max_digits=32)
    unit = models.ForeignKey(Unit, on_delete=models.PROTECT, null=True)
    info = models.CharField(max_length=200, null=True, blank=True)

    def __str__(self):
        return self.name

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
