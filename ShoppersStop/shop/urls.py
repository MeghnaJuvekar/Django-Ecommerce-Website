from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='shophome'),
    path('about/', views.about, name='aboutus'),
    path('contact/', views.contact, name='contactus'),
    path('tracker/', views.tracker, name='trackingstatus'),
    path('contact/', views.contact, name='contact'),
    path('search/', views.search, name='search'),
    path('products/<int:id>', views.productview, name='productview'),
    path('checkout/', views.checkout, name='checkout'),
    
]
