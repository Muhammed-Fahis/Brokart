from django.shortcuts import render

# Create your views here.
def show_cart(requst):
    return render(requst,'cart.html')