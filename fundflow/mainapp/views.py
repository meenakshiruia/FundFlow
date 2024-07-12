from django.shortcuts import render, HttpResponse, redirect
from .models import Borrower, Lender


# Create your views here.
def home(request):
    return render(request, "Home.html")


def borrower_signup(request):
    return render(request, "Investor-signup.html")


def lender_signup(request):
    return render(request, "startup-signup.html")


def success(request):
    return render(request, "success.html")

def saveBorrower(request):
    if request.method=="POST":
        name = request.POST.get('name')
        email = request.POST.get('email')
        password = request.POST.get('password')
        data = Borrower(name=name, email=email, password=password)
        data.save()
        return redirect('success')
    return render(request, "Investor-signup.html")

def saveLender(request):
    if request.method == "POST":
        name = request.POST.get('name')
        email = request.POST.get('email')
        password = request.POST.get('password')
        data = Lender(name=name, email=email, password=password)
        data.save()
        return redirect('success')
    return render(request, "startup-signup.html")
