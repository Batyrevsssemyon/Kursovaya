from django.contrib import admin
from .models import Product
from .models import Order
from .models import ProductOrder

admin.site.register(Product)
admin.site.register(Order)
admin.site.register(ProductOrder)



