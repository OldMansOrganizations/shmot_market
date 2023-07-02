from django.shortcuts import render
from .models import Products
# Create your views here.


def index(request):
    products = Products.objects.all()
    context = {'title': 'Главная', 'products': products}
    return render(request, 'catalog/index.html', context=context)
