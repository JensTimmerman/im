from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from django.views import generic

from .models import PantryItemLine

# Create your views here.


def index(request):
    return render(request, "inventory/index.html")


def consume(request):
    return render(request, "inventory/consume.html")


def shoppinglist(request):
    return render(request, "inventory/shoppinglist.html")


class Expirations(generic.ListView):
    template_name = "inventory/expirations.html"
    context_object_name = 'pis'

    def get_queryset(self):
        return PantryItemLine.objects.order_by('-expiry_date')


class DetailView(generic.DetailView):
    model = PantryItemLine
