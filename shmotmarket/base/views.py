from django.shortcuts import render
from .models import Products, Categories
# Create your views here.


def index(request):
    products = Products.objects.all()
    categories = Categories.objects.all()
    context = {'title': 'Главная', 'products': products, 'base': categories}
    return render(request, 'base/index.html', context=context)

