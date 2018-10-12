# Generated by Django 2.1.2 on 2018-10-07 11:08

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('inventory', '0016_auto_20180930_1409'),
    ]

    operations = [
        migrations.CreateModel(
            name='ShoppingListItem',
            fields=[
                ('pantryitem_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='inventory.PantryItem')),
            ],
            bases=('inventory.pantryitem',),
        ),
        migrations.AlterField(
            model_name='pantryitem',
            name='location',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='inventory.Location'),
        ),
    ]