from django.shortcuts import render
from . models import Product

# Create your views here.
def index(requst):
    return render(requst,'index.html')

def list_products(requst):


    return render(requst,'products.html',)

def detail_product(requst):
    return render(requst,'product_detail.html')