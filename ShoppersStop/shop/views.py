from django.shortcuts import render
from django.http import HttpResponse
from .models import Product, Contact, Orders, OrderUpdate
from math import ceil
import json
# Create your views here.
def home(request):
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
    thank =False
    if request.method == "POST":
        name = request.POST.get('name','')
        email = request.POST.get('email','')
        phone = request.POST.get('phone','')
        desc = request.POST.get('desc','')
        contact = Contact(name=name, email=email, phone=phone, desc=desc)
        contact.save()
        thank =True
    return render(request,"shop/contact.html",{'thank': thank})

def tracker(request):
    if request.method == "POST":
        orderid = request.POST.get('orderid','')
        email = request.POST.get('email','')
        try:
            order = Orders.objects.filter(order_id=orderid,email=email)
            if len(order)>0:
                update= OrderUpdate.objects.filter(order_id=orderid)
                updates =[]
                for item in update:
                    updates.append({'text':item.update_desc,'time':item.timestamp})
                    response = json.dumps([updates,order[0].items_json],default=str)
                return HttpResponse(response)
            else:
                return HttpResponse('{}')
        except Exception as e:
            return HttpResponse('{}')
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
        update = OrderUpdate(order_id= order.order_id, update_desc = "Your order has been placed")
        update.save()
        thank =True
        id = order.order_id
        return render(request,"shop/checkout.html",{'thank':thank,'id':id})
    return render(request,"shop/checkout.html")
