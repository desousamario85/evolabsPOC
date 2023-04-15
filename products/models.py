from django.db import models
from djchoices import DjangoChoices, ChoiceItem

# Create your models here.

class tech(DjangoChoices):
    PowerBI = ChoiceItem(1,'Power BI')
    PowerApps = ChoiceItem(2, 'Power Apps')
    PowerAutomate = ChoiceItem(3, 'Power Apps')
    PowerVA = ChoiceItem(4, 'Power Virtual Agents')
    Android = ChoiceItem(5, 'Android')
    iOS = ChoiceItem(6, 'iOS')
    Javascript = ChoiceItem(7, 'JavaScript')
    React = ChoiceItem(8, 'React')
    Django = ChoiceItem(9, 'Django')
    DocuSign = ChoiceItem(10, 'DocuSign')
    Stripe = ChoiceItem(11, 'Stripe')
    


class Category(models.Model):

    class Meta:
        verbose_name_plural = 'Categories'

    name =  models.CharField(max_length=254)
    friendly_name = models.CharField(max_length=254 , null=True, blank=True)


    def __str__(self):
        return self.name

    def get_friendly_name(self):
        return self.friendly_name

class Product(models.Model):
    category = models.ForeignKey('Category', null=True, blank=True, on_delete=models.SET_NULL)
    sku = models.CharField(max_length=254, null=True, blank=True)
    name = models.CharField(max_length=254)
    description = models.TextField()
    price = models.DecimalField(max_digits=6, decimal_places=2)
    rating = models.DecimalField(max_digits=6, decimal_places=2, null=True, blank=True)
    image_url = models.URLField(max_length=1024, null=True, blank=True)
    image = models.ImageField(null=True, blank=True)
    version = models.FloatField(null=True, blank=True)
    last_update = models.CharField(max_length=50,null=True, blank=True)
    tags = models.CharField(max_length=50, choices=tech.choices)
    license = models.TextField()

    def __str__(self):
        return self.name