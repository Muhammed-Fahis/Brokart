from django.shortcuts import render
from . models import Product
from django.core.paginator import Paginator

# Create your views here.
def index(requst):
    featured_products=Product.objects.order_by('priority')[:4]
    latest_products=Product.objects.order_by('-id')[:4]
    context={
        'featured_products':featured_products,
        'latest_products':latest_products
    }
    return render(requst,'index.html',context)

def list_products(requst):
    page=1
    if requst.GET:
         page=requst.GET.get('page',1)
    list_products=Product.objects.order_by('priority')
    product_paginator=Paginator(list_products,2)
    list_products=product_paginator.get_page(page)
    context={'products':list_products }
    return render(requst,'products.html',context)

def detail_product(requst,pk):
    product=Product.objects.get(pk=pk)
    context={'product':product}
    return render(requst,'product_detail.html',context)