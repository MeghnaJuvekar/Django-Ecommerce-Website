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
    return render(request,"shop/tracker.html")

def search(request):
    return render(request,"shop/search.html")

def productview(request,id):
    # Fetch Product using the Id
    product = Product.objects.filter(id=id)
    return render(request,"shop/productview.html",{'product':product[0]})

def checkout(request):
    return render(request,"shop/ceckout.html")
