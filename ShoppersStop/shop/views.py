from django.shortcuts import render
from django.http import HttpResponse
from .models import Product, Contact, Orders
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
    if request.method == "POST":
        name = request.POST.get('name','')
        email = request.POST.get('email','')
        phone = request.POST.get('phone','')
        desc = request.POST.get('desc','')
        contact = Contact(name=name, email=email, phone=phone, desc=desc)
        contact.save()
    return render(request,"shop/contact.html")

def tracker(request):
    return render(request,"shop/tracker.html")

def search(request):
    return render(request,"shop/search.html")

def productview(request,id):
    # Fetch Product using the Id
    product = Product.objects.filter(id=id)
    return render(request,"shop/productview.html",{'product':product[0]})

def checkout(request):
    if request.method == "POST":
        items_json = request.POST.get('itemsJson','')
        name = request.POST.get('name','')
        email = request.POST.get('email','')
        phone = request.POST.get('phone','')
        address = request.POST.get('address1','')+ " " +request.POST.get('address2','')
        # address = request.POST.get('address','')
        city = request.POST.get('city','')
        state = request.POST.get('state','')
        zip_code = request.POST.get('zip_code','')
        order = Orders(items_json=items_json, name=name, email=email, phone=phone, address=address, city=city, state=state,zip_code=zip_code)
        order.save()
        thank =True
        id = order.order_id
        return render(request,"shop/checkout.html",{'thank':thank,'id':id})
    return render(request,"shop/checkout.html")
