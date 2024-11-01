from django.shortcuts import render

# Create your views here.
def show_account(requst):
    return render(requst,'account.html')