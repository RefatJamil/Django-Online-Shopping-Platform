from django.shortcuts import render
from django.views import View
from .models import Customer, Product, Cart, OrderPlaced
from .forms import CoustomerRegistrationFrom
from django.contrib import messages


# def home(request):
#  return render(request, 'app/home.html')

class ProductView(View):
    def get(self, request):
        topwears = Product.objects.filter(category='TM')
        bottomewears = Product.objects.filter(category='BW')
        mobiles = Product.objects.filter(category='M')
        laptops = Product.objects.filter(category='L')

        context = {'topwears':topwears, 'bottomewears':bottomewears, 'mobiles':mobiles, 'laptops':laptops}

        return render(request, 'app/home.html', context)

class ProductDetailView(View):
    def get(self, request, pk):
        product = Product.objects.get(pk=pk)

        context = {'product':product}

        return render(request, 'app/productdetail.html', context)


def add_to_cart(request):
 return render(request, 'app/addtocart.html')

def buy_now(request):
 return render(request, 'app/buynow.html')

def profile(request):
 return render(request, 'app/profile.html')

def address(request):
 return render(request, 'app/address.html')

def orders(request):
 return render(request, 'app/orders.html')



def mobile(request, data=None):
    if data == None:
        mobile = Product.objects.filter(category='M')
    elif data == 'below':
        mobile = Product.objects.filter(category='M').filter(discounted_price__lt=10000)
    elif data == 'above':
        mobile = Product.objects.filter(category='M').filter(discounted_price__gt=10000)    
    else:
        mobile = Product.objects.filter(category='M').filter(brand=data)


    allmobile = Product.objects.filter(category='M')

    context = {
        'mobile':mobile,
        'allmobile':allmobile,
        } 
      
    return render(request, 'app/mobile.html', context)

def laptop(request, data=None):
    if data == None:
        laptop = Product.objects.filter(category='L')
    elif data == 'below':
        laptop = Product.objects.filter(category='L').filter(discounted_price__lt=35000)
    elif data == 'above':
        laptop = Product.objects.filter(category='L').filter(discounted_price__gt=35000)    
    else:
        laptop = Product.objects.filter(category='L').filter(brand=data)


    alllaptop = Product.objects.filter(category='L')

    context = {
        'laptop':laptop,
        'alllaptop':alllaptop,
        } 
      
    return render(request, 'app/laptop.html', context)

def topwear(request, data=None):
    if data == None:
        topwear = Product.objects.filter(category='TM')
    elif data == 'below':
        topwear = Product.objects.filter(category='TM').filter(discounted_price__lt=35000)
    elif data == 'above':
        topwear = Product.objects.filter(category='TM').filter(discounted_price__gt=35000)    
    else:
        topwear = Product.objects.filter(category='TM').filter(brand=data)


    alltopwear = Product.objects.filter(category='TM')

    context = {
        'topwear':topwear,
        'alltopwear':alltopwear,
        } 
      
    return render(request, 'app/topwear.html', context)

def bottomwear(request, data=None):
    if data == None:
        bottomwear = Product.objects.filter(category='BW')
    elif data == 'below':
        bottomwear = Product.objects.filter(category='BW').filter(discounted_price__lt=35000)
    elif data == 'above':
        bottomwear = Product.objects.filter(category='BW').filter(discounted_price__gt=35000)    
    else:
        bottomwear = Product.objects.filter(category='BW').filter(brand=data)


    allbottomwear = Product.objects.filter(category='BW')

    context = {
        'bottomwear':bottomwear,
        'allbottomwear':allbottomwear,
        } 
      
    return render(request, 'app/bottomwear.html', context)

def login(request):
 return render(request, 'app/login.html')

# def customerregistration(request):
#  return render(request, 'app/customerregistration.html')

class CustomerRegistrationView(View):
    def get(self, request):
      form = CoustomerRegistrationFrom()
      context = {'form': form}
      return render(request, 'app/customerregistration.html', context)
    
    def post(self, request):
        form = CoustomerRegistrationFrom(request.POST)
        if form.is_valid():
           messages.success(request, 'Congratulation !! Account Registered Successfully.')
           form.save()
        context = {'form': form}
        return render(request, 'app/customerregistration.html', context)

def checkout(request):
 return render(request, 'app/checkout.html')
