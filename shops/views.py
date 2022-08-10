from tokenize import String
from django.shortcuts import render
from .models import IceCream
from django.http import Http404



# def get_ice_cream(request, ice_cream_id):
#     ice_cream = IceCream.objects.get(id=ice_cream_id)
#     context = {
#         'name': ice_cream.name,
# #        "flavors": ice_cream.flavors.values_list('name'),
#         "shop": ice_cream.shop,
#         "stock": ice_cream.stock,
#     }
#     print(context)
#     return render(request, 'ice_cream_detail.html', context)


def get_ice_cream(request, ice_cream_id):
    try:
        ice_cream = IceCream.objects.get(id=ice_cream_id)
    except IceCream.DoesNotExist:
        raise Http404("Ice Cream does not exist")
    context = {
        'name': ice_cream.name,
        "flavors": ice_cream.flavors.values_list('name'),
        "shop": ice_cream.shop,
        "stock": ice_cream.stock,
    }
    print(context)
    return render(request, 'ice_cream_detail.html', context)


    """
    List View
Go to shops/views.py and add a get_ice_creams view function that takes in a request and renders a template named ice_cream_list.html.
Your context should include the names, flavors (as a list of strings), and shop names of all ice creams.
Add your get_ice_creams view to bareed/url.py and name it ice-cream-list.
Create a templates folder inside of shops and add an ice_cream_list.html file.
The template should render the entire context passed to it.
Use this link to see how to loop over objects in DTL.
Run the server and check out your beautiful ice creams.
Run the tests using pytest -m list and pass all tests.
Commit your code and push."""


"""Your context should include the names, flavors (as a list of strings), and shop names of all ice creams."""
# def get_ice_creams(request):
#     ice_creams = IceCream.objects.all()
#     context = {
#         'name': ice_creams.name,
#         "flavors": ice_creams.flavors.values_list('name'),
#         "shop": ice_creams.shop,
#     }
#     return render(request, 'ice_cream_list.html', context)




def get_ice_creams(request):
    ice_creams = IceCream.objects.all()
    context = {
#List Comprehension
        "name": ice_creams.name,
        "flavors": ice_creams.flavors.values_list("name"),
        "shop": ice_creams.shop
    }
    # ice_creams = IceCream.objects.all()
    # print(dir(ice_creams))
    return render(request, 'ice_cream_list.html', context)