from django.shortcuts import render
from django.http import HttpResponse
from .models import Product
def product_details(request):
    obj= Product.objects.get(id=1)
    '''context={
        'title':obj.title,
        'description': obj.description
    }'''
    context={
        'object':obj
    }
    return render(request, 'products/details.html', context)

def about_pages(request):
    return HttpResponse('welcome to about page')

# Create your views here.
