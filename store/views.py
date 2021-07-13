from django.shortcuts import render
from .models import Cartitems, Customer, Product,Cart

# Create your views here.
def store(request):
    products = Product.objects.all()
    
    if request.user.is_authenticated:
        customer = request.user.customer
        cart,created = Cart.objects.get_or_create(customer = customer,completed = False) 
        cartitems = cart.cartitems_set.all()
        
    return render(request,'store.html',{'products':products,'cartitems':cartitems})

def checkout(request):
    return render(request,'store.html')
