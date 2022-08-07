from tokenize import String
from django.shortcuts import render
from .models import IceCream


# Create your views here.
# Go to shops/views.py and add a get_ice_cream view function that takes in a request and ice_cream_id, and renders a template named ice_cream_detail.html (you might find this link useful).
# Fetch the ice cream object based on the id received in the parameter.
# Add the following context to be injected into your template:
# name: the ice cream's name as a string.
# shop: the ice cream's shop name as a string.
# stock: the ice cream's current stock as an integer.

def get_ice_cream(request, ice_cream_id):
    ice_cream = IceCream.objects.get(id=ice_cream_id)
    context = {
        'name': ice_cream.name,
        "flavors": ice_cream.flavors.values_list('name'),
        "shop": ice_cream.shop,
        "stock": ice_cream.stock,
    }
    print(context)
    return render(request, 'ice_cream_detail.html', context)
