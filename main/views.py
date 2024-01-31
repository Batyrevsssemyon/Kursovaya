from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import ProductSerializer
from .models import Product
from .models import Order
from .models import ProductOrder

# Create your views here.

def index(request):
    products = Product.objects.all()

    return render(request, 'main/index.html', {'data': products})

def check(request):
    products = Product.objects.all()

    address, latitude, longitude = request.POST.get("address", "Undefined").split(";")

    order = Order()
    order.address = address
    order.latitude = latitude
    order.longitude = longitude
    order.save()

    for product in products:
        if int(request.POST.get("num" + str(product.id), 0)) > 0:
            productOrder = ProductOrder()
            productOrder.productId = product.id
            productOrder.orderId = Order.objects.last().id
            productOrder.quantity = int(request.POST.get("num" + str(product.id), 0))
            productOrder.save()

    productOrders = ProductOrder.objects.filter(orderId = Order.objects.last().id)

    list = []
    total = 0
    for product in products:
        for productOrder in productOrders:
            if product.id == productOrder.productId:
                el = {'title': product.title, 'amount': product.amount, 'quantity': productOrder.quantity}
                list.append(el)
                total += product.amount * productOrder.quantity

    order = Order.objects.last()

    return render(request, 'main/check.html', {'order': order, 'products': list, 'total': total})

def response(request):
    order = Order.objects.last()

    address = order.address
    latitude = order.latitude
    longitude = order.longitude

    return render(request, 'main/response.html', {'address': address, 'latitude': latitude, 'longitude': longitude})

class ProductView(APIView):
    def get(self, request):
        products = Product.objects.all()
        serializer = ProductSerializer(products, many=True)
        return Response({"products": serializer.data})