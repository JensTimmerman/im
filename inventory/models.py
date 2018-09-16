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
)


class PantryItem(models.Model):
    name =  models.CharField(max_length=200)
    category = models.CharField(max_length=200, choices=CATEGORIES)
    min_quantity = models.IntegerField(default=1)

    def __str__(self):
        return self.name

class PantryItemLine(models.Model):
    pantry_item = models.ForeignKey(PantryItem, on_delete=models.PROTECT, default='UN' )
    quantity = models.IntegerField(default=1)
    expiry_date = models.DateField()

    def __str__(self):
        return self.pantry_item.name + ' ' + self.quantity
