from django.shortcuts import render
from django.http import HttpResponse
from .models import BlogPost

# Create your views here.
def blog(request):
    myposts = BlogPost.objects.all()
    return render(request,"blog/index.html",{'myposts':myposts})

def blogpost(request,id):
    post = BlogPost.objects.filter(post_id = id)[0]
    print(post)
    return render(request,"blog/blogpost.html",{'post':post})