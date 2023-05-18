from django.contrib import admin
from . models import Product,Order,Order_Item
# Register your models here.
class Order_itemAll(admin.TabularInline):
    model=Order_Item
class OrderAdmin(admin.ModelAdmin):
    inlines=[Order_itemAll]
admin.site.register(Product)
admin.site.register(Order,OrderAdmin)
admin.site.register(Order_Item)
