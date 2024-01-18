from django.shortcuts import render
from .models import *
# Create your views here.
 
def index(request):
    product_objects = Product.objects.all()
    for i in product_objects:
        print(i.title)
    return render(request,'shop/index.html',{'product_objects':product_objects,})