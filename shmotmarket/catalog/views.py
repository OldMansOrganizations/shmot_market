from django.shortcuts import render
from .models import Products, Categories
# Create your views here.


def index(request):
    products = Products.objects.all()
    categories = Categories.objects.all()
    context = {'title': 'Главная', 'products': products, 'catalog': categories}
    return render(request, 'catalog/index.html', context=context)
