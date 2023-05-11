from django.contrib import admin
from apps.products.models import Products, Currency
# Register your models here.
admin.site.register(Products)
admin.site.register(Currency)