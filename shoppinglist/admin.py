from django.contrib import admin
from.models import ListItem, Product, Shop

@admin.register(ListItem)
class ListItem(admin.ModelAdmin):
    list_display = ['product', 'amount', 'price', 'shop']

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['name']

@admin.register(Shop)
class ShopAdmin(admin.ModelAdmin):
    list_display = ['name']