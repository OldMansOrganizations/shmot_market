from django.shortcuts import render
from base.models import Products, Categories, SubCategories

# Create your views here.


def index(request):
    products = Products.objects.all()
    categories = Categories.objects.all()
    subcategories = SubCategories.objects.all()
    context = {'title': 'Категории', 'products': products, 'categories': categories, 'subcategories': subcategories}
    return render(request, 'categories/categories.html', context=context)
