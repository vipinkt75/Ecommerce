from django.shortcuts import render
from . models import Product
from django.contrib.auth.models import User
from django.shortcuts import redirect
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required
from cart.cart import Cart
from . models import Order,Order_Item



# Create your views here.

def index(request):

    dictionary={
        'produ':Product.objects.all()
    }
    return render(request,'index.html',dictionary)

def cart(request):

    return render(request,'cart.html')

def checkout(request):

    return render(request,'checkout.html')

def tkx(request):

    return render(request,'tkx.html')


def placehoder(request):


    if request.method=="POST":
        uid=request.session.get('_auth_user_id')
        user=User.objects.get(id=uid)
        
        cart=request.session.get('cart')
        firstname = request.POST.get('firstname')
        
        last_name = request.POST.get('lastname')
        company = request.POST.get('company')
        country = request.POST.get('country')
        address = request.POST.get('address')
        state = request.POST.get('state')
        city = request.POST.get('city')
        pin = request.POST.get('pin')
        phone= request.POST.get('phone')
        email= request.POST.get('email')
        amount= request.POST.get('amount')

        
        order=Order(
            user=user,
            first_name=firstname,
            last_name=last_name,   
            country=country,
            address =address,
            city=city,
            state =state,
            post=pin,
            email=email,
            
            amount=amount,

            
        
        
        )
        order.save()


        for i in cart:
            a=float(cart[i]['price'])
            b=int(cart[i]['quantity'])
            total=a*b
            item=Order_Item(
            order=order,
            product=cart[i]['name'],
            image=cart[i]['image'],
            quantity=cart[i]['quantity'],
            price=cart[i]['price'],
            total=total


            )
            item.save()


    return render(request,'placeorder.html')


def signin(request):

    if request.method=="POST":
        username=request.POST.get('username')
        password=request.POST.get('password')
        
        user = authenticate(username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('index')
        else:
            return redirect('signup')


    return render(request,'account/signin.html')


def signup(request):

    if request.method=="POST":
        username=request.POST.get('username')
        firstname=request.POST.get('first_name')
        lastname=request.POST.get('last_name')
        email=request.POST.get('email')
        password=request.POST.get('password')
        password2=request.POST.get('password2')

        customer = User.objects.create_user(username,email,password)
        customer.first_name=firstname
        customer.last_name=lastname
        customer.save()
        return redirect('signin')



    return render(request,'account/signup.html')


def logout2(request):
    logout(request)
    return redirect('index')







@login_required(login_url="/users/login")
def cart_add(request, id):
    cart = Cart(request)
    product = Product.objects.get(id=id)
    cart.add(product=product)
    return redirect("index")


@login_required(login_url="/users/login")
def item_clear(request, id):
    cart = Cart(request)
    product = Product.objects.get(id=id)
    cart.remove(product)
    return redirect("cart_detail")


@login_required(login_url="/users/login")
def item_increment(request, id):
    cart = Cart(request)
    product = Product.objects.get(id=id)
    cart.add(product=product)
    return redirect("cart_detail")


@login_required(login_url="/users/login")
def item_decrement(request, id):
    cart = Cart(request)
    product = Product.objects.get(id=id)
    cart.decrement(product=product)
    return redirect("cart_detail")


@login_required(login_url="/users/login")
def cart_clear(request):
    cart = Cart(request)
    cart.clear()
    return redirect("cart_detail")


@login_required(login_url="/users/login")
def cart_detail(request):
    return render(request, 'cart.html')