from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from django.views import generic
from django.views.generic.edit import CreateView, DeleteView, UpdateView
from django.db.models import F, Sum


from .models import PantryItem, PantryItemLine

# Create your views here.


def index(request):
    return render(request, "inventory/index.html")


def consume(request):
    return render(request, "inventory/consume.html")


def add(request):
    return render(request, "inventory/add.html")

class Shoppinglist(generic.ListView):
    template_name = "inventory/shoppinglist.html"
    context_object_name = 'pis'

    def get_queryset(self):
        return PantryItem.objects.annotate(total_quantity=Sum(F('pantryitemline__quantity') * F('pantryitemline__size'))).filter(min_quantity__gt=F('total_quantity'))
        #return PantryItemLine.objects.filter(quantity__lt=F('pantry_item__min_quantity'))



class Expirations(generic.ListView):
    template_name = "inventory/expirations.html"
    context_object_name = 'pis'

    def get_queryset(self):
        return PantryItemLine.objects.exclude(expiry_date__isnull=True).order_by('expiry_date')


class DetailView(generic.DetailView):
    model = PantryItemLine
