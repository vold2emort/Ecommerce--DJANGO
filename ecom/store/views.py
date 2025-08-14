from django.shortcuts import render, redirect
from .models import Product
from django.contrib.auth import login, logout, authenticate
from django.contrib import messages
from .forms import SignUpForm


# Create your views here.
def home(request):
    product = Product.objects.all()
    return render(request, 'store/index.html', {"products": product})

def about(request):
    return render(request, 'store/about.html')

def login_user(request):
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request=request, user=user)
            messages.success(request, "You have been logged in successfully.")
            return redirect('home')
        else:
            messages.error(request, ("Invalid username or password."))
            return redirect('login')
    return render(request, 'store/login.html')

def logout_user(request):
    logout(request)
    messages.success(request, ("You have been logged out successfully."))
    return redirect('home')

def register_user(request):
    form = SignUpForm()
    if request.method == "POST":
         form = SignUpForm(request.POST)
         if form.is_valid():
             form.save()
             username = form.cleaned_data["username"]
             password = form.cleaned_data["password1"]
             user = authenticate(username=username, password=password)
             login(request, user)
             messages.success(request, "You have registered successfully.")
             return redirect('home')
         else:
            messages.error(request, "Registration failed. Please correct the errors below.")
    return render(request, 'store/register.html', {"form": form})


def product(request, id):
    product = Product.objects.get(id=id)
    return render(request, 'store/product.html', {"product": product})