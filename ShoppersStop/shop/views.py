from django.shortcuts import render
from django.http import HttpResponse
from .models import Product
from math import ceil

# Create your views here.

def home(request):
    # products = Product.objects.all()
    
    # params = {'no_of_slides':nslides,'range':range(1,nslides),'product':products}
    # allProds = [[products,range(1,nslides),nslides],
    #             [products,range(1,nslides),nslides]]
    allProds = []
    catprods = Product.objects.values('category','id')
    cats = {item['category'] for item in catprods}
    for cat in cats:
        prod = Product.objects.filter(category=cat)
        n = len(prod)
        nslides = n//4 + ceil((n/4)-(n//4))
        allProds.append([prod, range(1,nslides),nslides])
    params = {'allProds':allProds}
    return render(request,"shop/home.html", params)

def about(request):
    return render(request,"shop/about.html")

def contact(request):
    return HttpResponse("contact")

def tracker(request):
    return HttpResponse("tracker")

def search(request):
    return HttpResponse("search")

def productview(request):
    return HttpResponse("productview")

def checkout(request):
    return HttpResponse("checkout")

