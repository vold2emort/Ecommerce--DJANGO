from django.shortcuts import render
from .models import Product

# Create your views here.
def home(request):
    product = Product.objects.all()
    return render(request, 'store/index.html', {"products": product})