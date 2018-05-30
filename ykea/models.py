# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models


# Create your models here.
from django.db.models import ManyToManyField
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

class Item(models.Model):
    CATEGORIES = (
        ("beds", "Beds & mattressess"),
        ("furn", "Furniture, wardrobes & shelves"),
        ("sofa", "Sofas & armchairs"),
        ("table", "Tables & chairs"),
        ("texti", "Textiles"),
        ("deco", "Decoration & mirrors"),
        ("light", "Lighting"),
        ("cook", "Cookware"),
        ("table", "Tableware"),
        ("taps", "Taps & sinks"),
        ("org", "Organisers & storage accesories"),
        ("toys", "Toys"),
        ("leis", "Leisure"),
        ("safe", "safety"),
        ("diy", "Do-it-yourself"),
        ("floor", "Flooring"),
        ("plant", "Plants & gardering"),
        ("food", "Food & beverages")
    )
    item_number = models.CharField(max_length=8, unique=True)
    name = models.CharField(max_length=50)
    description = models.TextField()
    price = models.DecimalField(max_digits=8, decimal_places=2)
    is_new = models.BooleanField()
    size = models.CharField(max_length=40)
    instructions = models.FileField()
    featured_photo = models.ImageField()
    category = models.CharField(max_length=5, choices=CATEGORIES)

    def __str__(self):
        return ('[**NEW**]' if self.is_new else '') +\
               "[" + self.category + "] [" + self.item_number + "] " + self.name +\
               " - " + self.description + " (" + self.size + ") : " + str(self.price) + " €"

class Shoppingcart(models.Model):
    id = models.CharField(max_length=8, unique=True, primary_key=True)
    items = models.ManyToManyField(Item, through='ItemQuantity')


class ItemQuantity(models.Model):
    cart = models.ForeignKey('Shoppingcart')
    item = models.ForeignKey('Item')
    quantity = models.PositiveIntegerField()

class Client(models.Model):
    client = models.OneToOneField(User, on_delete=models.CASCADE)
    cash = models.DecimalField(max_digits = 20, decimal_places = 2)
    #shoppingcart = models.OneToOneField(Shoppingcart, on_delete=models.CASCADE)
    def __str__(self):
        return str(self.client.username)

@receiver(post_save, sender=User)
def create_user_client(sender, instance, created, **kwargs):
    if created:
        Client.objects.create(client=instance, cash = 50)

@receiver(post_save, sender=User)
def save_user_client(sender, instance, **kwargs):
    try:
        instance.client.save()
    except:
        Client.objects.create(client=instance, cash = 50)
