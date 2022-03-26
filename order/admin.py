from django.contrib import admin
from order.models import  Cart, Order, OrderItem,Transaction
# Register your models here.
admin.site.register(Cart)
admin.site.register(OrderItem)
admin.site.register(Order)
admin.site.register(Transaction)