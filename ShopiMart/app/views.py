from django.shortcuts import render, redirect
from django.views import View
from .models import Customer, Product, Cart, OrderPlaced
from .forms import CoustomerRegistrationFrom, CustomerProfileForm
from django.contrib import messages
from django.db.models import Q
from django.http import JsonResponse, HttpResponseBadRequest
from django.contrib.auth.decorators import login_required
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
        item_already_in_cart = False
        if request.user.is_authenticated:
            item_already_in_cart = Cart.objects.filter(Q(product=product.id) & Q(user=request.user)).exists()


        context = {'product':product, 'item_already_in_cart':item_already_in_cart}

        return render(request, 'app/productdetail.html', context)

@login_required
def add_to_cart(request):
    user = request.user
    product_id = request.GET.get('prod_id')
    product = Product.objects.get(id=product_id)

    if Cart.objects.filter(Q(product=product.id) & Q(user=request.user)).exists():
        return redirect(f'/product-detail/{product_id}')

    cart = Cart(user=user, product=product)
    print(cart)

    cart.save()

    return redirect(f'/product-detail/{product_id}')

@login_required
def show_cart(request):
    if request.user.is_authenticated:
        user = request.user
        carts = Cart.objects.filter(user=user)
        amount = 0.0
        shipping_amount = 70.0  
        cart_product = [p for p in Cart.objects.all() if p.user == user]

        if cart_product:
            for p in cart_product:
                temp_amount = (p.quantity * p.product.discounted_price)
                amount += temp_amount
        if amount == 0:
            total_amount = 0.0
        else:    
            total_amount = shipping_amount + amount

    context={'carts': carts, 'amount':amount, 'total_amount':total_amount}
    return render(request, 'app/addtocart.html', context)

@login_required
def plus_cart(request):
    if request.method =="GET":
        prod_id = request.GET['prod_id']
        c = Cart.objects.get(Q(product=prod_id) & Q(user=request.user))
        c.quantity+=1
        c.save()
        amount = 0.0
        shipping_amount = 70.0  
        cart_product = [p for p in Cart.objects.all() if p.user == request.user]
        if cart_product:
            for p in cart_product:
                temp_amount = (p.quantity * p.product.discounted_price)
                amount += temp_amount
        if amount == 0:
            total_amount = 0.0
        else:    
            total_amount = shipping_amount + amount

        data = {
            'quantity': c.quantity,
            'amount':amount,
            'total_amount':total_amount
            }
        return JsonResponse(data)


@login_required
def minus_cart(request):
    if request.method =="GET":
        prod_id = request.GET['prod_id']
        c = Cart.objects.get(Q(product=prod_id) & Q(user=request.user))
        if c.quantity != 1:
            c.quantity-=1
            c.save()
        amount = 0.0
        shipping_amount = 70.0  
        cart_product = [p for p in Cart.objects.all() if p.user == request.user]
        if cart_product:
            for p in cart_product:
                temp_amount = (p.quantity * p.product.discounted_price)
                amount += temp_amount
        if amount == 0:
            total_amount = 0.0
        else:    
            total_amount = shipping_amount + amount

        data = {
            'quantity': c.quantity,
            'amount':amount,
            'total_amount':total_amount
            }
        return JsonResponse(data)
    
@login_required
def remove_from_cart(request, id):
    p = Cart.objects.get(id=id)
    print(p)
    p.delete()
    return redirect('/cart')



@login_required
def buy_now(request):
 return render(request, 'app/buynow.html')


class ProfileView(View):
    def get(self, request):
        form = CustomerProfileForm()
        context = {'form':form, 'active':'btn-dark'}
        return render(request, 'app/profile.html', context)
        
    def post(self, request):
        form = CustomerProfileForm(request.POST)
        if form.is_valid():
            user = request.user
            name = form.cleaned_data['name'] 
            locality = form.cleaned_data['locality']
            city = form.cleaned_data['city'] 
            zipcode = form.cleaned_data['zipcode'] 
            state = form.cleaned_data['state']
            reg = Customer(user=user, name=name, locality=locality, city=city, state=state, zipcode=zipcode)
            reg.save()
            messages.success(request, 'Congratulation !! Profile Updated Successfully.')
            context = {'form':form, 'active':'btn-primary'}
        return render(request, 'app/profile.html', context)

@login_required
def addaddress(request):
    add = Customer.objects.filter(user=request.user)
    context = {'active':'btn-dark', 'add':add}

    return render(request, 'app/address.html', context)

@login_required
def deladdress(request, id):
    user = Customer.objects.get(id=id)  
    user.delete()  
    return redirect("address")
 
@login_required
def orders(request):
 op = OrderPlaced.objects.filter(user= request.user)
 context={'op':op}
 return render(request, 'app/orders.html', context)



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
    
@login_required
def checkout(request):
    user = request.user
    addrs = Customer.objects.filter(user=user)
    cart_items = Cart.objects.filter(user=user)
    
    amount = 0.0
    shipping_amount = 70.0  
    cart_product = [p for p in Cart.objects.all() if p.user == request.user]
    if cart_product:
            for p in cart_product:
                temp_amount = (p.quantity * p.product.discounted_price)
                amount += temp_amount
            if amount == 0:
                total_amount = 0.0
            else:    
                total_amount = shipping_amount + amount
    else:
        messages.error(request,'Please add product before order placed')
        return redirect("show-cart")
            
    context={'addrs':addrs, 'cart_items':cart_items, 'total_amount':total_amount}
    return render(request, 'app/checkout.html', context)

@login_required
def paymentdone(request):
    user = request.user
    custid = request.GET.get('custid')
    customer = Customer.objects.get(id=custid)
    cart = Cart.objects.filter(user=user)
    for c in cart:
        OrderPlaced(user=user, customer= customer, product=c.product, quantity=c.quantity).save()
        c.delete()

    return redirect("orders")    
