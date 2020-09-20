from django.shortcuts import render
from mystore.models import Product
from datetime import datetime
from cart.cart import Cart
from cart.forms import CardAddProductForm
from mystore.forms import FormContact

# Create your views here.
def index(request):
    pro_list = Product.objects.order_by('name')
    pro_dict = {"products":pro_list }
    return render(request, "mystore/index.html", context=pro_dict)

def product_detail(request, id=None):
    product = Product.objects.get(pk=id)
    cart_product_form = CardAddProductForm()
    return render(request, 'mystore/product_detail.html', context= {'product': product, 'cart_product_form': cart_product_form})

def contact(request):
    registered = False
    if request.method == "POST":
        form_contact = FormContact(data = request.POST)
        if form_contact.is_valid():
            register = form_contact.save()
            register.save()
            registered = True
        else:
            print(form_contact.errors)
    else:
        form_contact = FormContact()
    return render(request, 'mystore/contact.html', {'contact_form':form_contact,'registered': registered})

def shop(request):
    pro_list = Product.objects.order_by('name')
    pro_dict = {"products":pro_list }
    return render(request, "mystore/shop.html", context=pro_dict)