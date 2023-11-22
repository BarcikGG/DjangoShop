from django.contrib import admin
from .models import Category, Tag, Product, Order, OrderItem

admin.site.register(Category)
admin.site.register(Tag)
admin.site.register(Product)
admin.site.register(Order)
admin.site.register(OrderItem)
