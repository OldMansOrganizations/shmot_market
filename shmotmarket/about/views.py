from django.shortcuts import render

# Create your views here.


def about(request):
	context = {'title': 'О комапании'}
	return render(request, 'about/about.html', context=context)
