# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import decimal

from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from ykea.models import Item, Shoppingcart, ItemQuantity, Client
from django.http import HttpResponseRedirect, HttpResponse
from django.core.urlresolvers import reverse
from django.contrib import auth
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.contrib.auth.decorators import login_required

from django.contrib.auth.models import User, Group
from rest_framework import viewsets
from .serializers import ItemSerializer

from rest_framework import permissions

class ItemViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows Items to be viewed or edited.
    """
    queryset = Item.objects.all().order_by('item_number')
    serializer_class = ItemSerializer




def index(request):
    return render(request, 'ykea/categories.html', context={"categories": Item.CATEGORIES})
    # return HttpResponse("")


def items(request, category=""):
    category_description = ""

    if category:
        items = Item.objects.filter(category=category)
        category_description = dict(Item.CATEGORIES)[category]
    else:
        items = Item.objects.all()

    context = {
        'items': items,
        'category': category_description
    }

    return render(request, 'ykea/items.html', context)


def product(request, item_number):
    try:
        item = Item.objects.get(item_number=item_number)
        context = {
            'product': item
        }
        return render(request, 'ykea/product.html', context)

    except Item.DoesNotExist or Item.MultipleObjectsReturned:
        return HttpResponse("404 watch your profanity")


@login_required
def shoppingcart(request):
    if "shoppingcart" in request.session:
        cart = Shoppingcart.objects.get(id=request.session["shoppingcart"])

    else:
        cart = Shoppingcart(id="klkjr5an")
        cart.save()

    for key in request.POST:
        if key.startswith("checkbox"):
            item = Item.objects.get(item_number=key[8:])
            try:
                if ItemQuantity.objects.get(cart=cart, item=item):
                    item_quantity = ItemQuantity.objects.get(cart=cart, item=item)
                    item_quantity.quantity += 1
                    item_quantity.save()

            except ItemQuantity.DoesNotExist:
                item_quantity = ItemQuantity(cart=cart, item=item, quantity=1)
                item_quantity.save()

    request.session["shoppingcart"] = cart.id

    return HttpResponseRedirect(reverse('buy'))


@login_required
def buy(request):
    cart = Shoppingcart.objects.get(id=request.session["shoppingcart"])
    item_quantities = ItemQuantity.objects.filter(cart=cart)

    context = {'item_quantities': item_quantities}

    return render(request, 'ykea/shoppingcart.html', context)


@login_required
def process(request):
    item_numbers = []

    for key in request.POST:
        if key.startswith("checkbox"):
            item_numbers += [key[8:]]

    request.session['item_numbers'] = item_numbers

    if "DELETE" in request.POST:
        return HttpResponseRedirect(reverse('delete'))

    if "CHECKOUT" in request.POST:
        return HttpResponseRedirect(reverse('checkout'))

    return HttpResponse("404 not found amigo")


@login_required
def delete(request):
    cart = Shoppingcart.objects.get(id=request.session["shoppingcart"])

    for item_number in request.session['item_numbers']:

        try:
            item = Item.objects.get(item_number=item_number)  # iterem els items de la checkbox

            item_quantity = ItemQuantity.objects.get(cart=cart, item=item)  # obtenim la quanitat de l'item seleccionat

            if item_quantity.quantity > 1:  # si n'hi ha més d'un, el decrementem
                item_quantity.quantity -= 1
                item_quantity.save()
            else:
                item_quantity.delete()  # si n'hi ha un, l'eliminem

        except Item.DoesNotExist:
            continue

    context = {'item_quantities': ItemQuantity.objects.filter(cart=cart)}

    return render(request, 'ykea/shoppingcart.html', context)

@login_required
def checkout(request):
    cart = Shoppingcart.objects.get(id=request.session["shoppingcart"])
    item_quantities = ItemQuantity.objects.filter(cart=cart)

    total_price = 0.0
    for item_quantity in item_quantities:
        total_price += float(item_quantity.item.price) * item_quantity.quantity

    context = {'item_quantities': ItemQuantity.objects.filter(cart=cart),
               'total_price': total_price}

    client = Client.objects.get(client__username = auth.get_user(request).username)
    if client.cash >= total_price:
        client.cash -= decimal.Decimal(total_price)
        client.save()
    else:
        return HttpResponse("You don't have enough money. Get out.")

    response = render(request, 'ykea/checkout.html', context)

    del request.session['shoppingcart']  # eliminem el shoppingcart de la sessió
    cart.delete()  # i de la base de dades, ja posats

    return response


def login_view(request, next_page="/ykea"):
    if request.method == 'POST':
        username = request.POST.get('username', '')
        password = request.POST.get('password', '')
        user = auth.authenticate(username=username, password=password)
        if user is not None and user.is_active:
            # Correct password, and the user is marked "active"
            auth.login(request, user)
            # Redirect to a success page.
            return HttpResponseRedirect("/account/loggedin/")
        else:
            # Show an error page
            return HttpResponseRedirect("/account/invalid/")
    else:
        form = UserCreationForm()

    return render(request, "registration/login.html", {'form': form})


def logout_view(request):
    auth.logout(request)
    # Redirect to a success page.
    return HttpResponseRedirect("/account/loggedout/")


def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            new_user = form.save()
            return HttpResponseRedirect(reverse("index"))
    else:
        form = UserCreationForm()
    return render(request, "registration/register.html", {
        'form': form,
    })


def buy_success(request):
    return None