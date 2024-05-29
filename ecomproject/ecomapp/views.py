from django.shortcuts import render,redirect
from django.conf.urls.static import static
from django.db import IntegrityError
from ecomapp.models import Item
from ecomapp.models import Product
from ecomapp.models import userr
from ecomapp.models import Cart
from django.conf import settings
from django.contrib.auth.models import User,auth
from django.contrib import messages
from django.shortcuts import render, get_object_or_404
from django.db.models import Sum
from django.db.models import F
from django.contrib.auth.decorators import login_required

import os

def home(request):
    if request.user.is_authenticated:
        it = Item.objects.all()
        try:
            us = userr.objects.get(user_name=request.user)
        except userr.DoesNotExist:
            us = None

        return render(request, 'index.html', {'ite': it, 'use': us})
    else:
        return render(request, 'index.html')


def login(request):
    if request.user.is_authenticated:
        it = Item.objects.all()
        return render(request,'login.html',{'ite':it})
    else:
        return render(request,'login.html')

def signup(request):
    if request.user.is_authenticated:
        it = Item.objects.all()
        return render(request,'signup.html',{'ite': it})
    else:
        return render(request,'signup.html')



def about(request):
    if request.user.is_authenticated:
        it = Item.objects.all()
        try:
            us = userr.objects.get(user_name=request.user)
        except userr.DoesNotExist:
            us = None
        return render(request,'about.html',{'ite': it,'use': us})
    else:
        return render(request,'about.html')      

def homenavbar(request):
    if request.user.is_authenticated:
        try:
            us = userr.objects.get(user_name=request.user)
        except userr.DoesNotExist:
            us = None
        return render(request, 'homenav.html', {'use': us})
    else:
        return render(request, 'homenav.html')

def usernavbar(request):
    if request.user.is_authenticated:
        it = Item.objects.all()
        return render(request, 'user/usernav.html', {'ite': it})


def loginfn(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        usr = auth.authenticate(username=username,password=password)
        if usr is not None:
            if usr.is_staff:
                auth.login(request,usr)
                return render(request,'admin/adminpage.html')
            else:
                auth.login(request,usr)
                it = Item.objects.all()
                try:
                    us = userr.objects.get(user_name=request.user)
                except userr.DoesNotExist:
                    us = None
                return render(request,'user/userpage.html',{'ite':it,'use':us})
        else:
            messages.error(request,'Invalid Username or Password')
            return redirect('login')
        
def adminhome(request):
    return render(request,'admin/adminpage.html') 

def add_item(request):
    return render(request,'admin/adcat.html')

def itemreg(request):
    if request.user.is_authenticated:
        if request.method == 'POST':
            cat_name = request.POST.get('cat_name')
            it = Item(itemname=cat_name)
            it.save()
            messages.success(request,'Category Added Successfully')
            return redirect('add_item')
        
def add_product(request):
    it = Item.objects.all()
    return render(request,'admin/adproduct.html',{'ite':it})

def productreg(request):
    if request.user.is_authenticated:
        if request.method == 'POST':
            cat_name = request.POST.get('sel')
            pro_name = request.POST.get('pdt_name')
            pro_price = request.POST.get('pdt_price')
            pro_des = request.POST.get('pdt_desc')
            pro_image = request.FILES.get('pdt_image')
            it = userr.objects.get(id=cat_name)
            pro = Product(catname=it,proname=pro_name,proprice=pro_price,prodes=pro_des,proimage=pro_image)
            pro.save()
            messages.success(request,'Product Added Successfully')
            return redirect('view_product')
        
def view_product(request):
    pro = Product.objects.all()
    return render(request,'admin/viewproduct.html',{'pro':pro})

def pdelete(request,pk):
    if request.user.is_authenticated:
        pro = Product.objects.get(id=pk)
        pro.delete()
        messages.success(request,'Product Deleted Successfully')
        return redirect('view_product')
        
def admin_logout(request):
    auth.logout(request)
    return redirect('home')

def userregg(request):
        if request.method == 'POST':
            firstname  = request.POST.get('fname')
            lastname = request.POST.get('lname')
            usrname = request.POST.get('uname')
            mail = request.POST.get('email')
            password = request.POST.get('pass')
            cpassword = request.POST.get('cpass')
            address = request.POST.get('address')
            contact = request.POST.get('contact')
            image = request.FILES.get('image')
            if password == cpassword:
                if User.objects.filter(username=usrname).exists():
                    messages.error(request,'Username Already Exists')
                    return redirect('signup')
                else:
                    usr = User.objects.create_user(username=usrname, email=mail, password=password,first_name=firstname,last_name=lastname)
                    us = userr(user_name=usr,useraddress=address,usernumber=contact,userimage=image)
                    usr.save()
                    us.save()
                    messages.success(request,'User Added Successfully')
                    return redirect('signup')
            else:
                messages.error(request,'Password Does Not Match')
                return redirect('signup')
            
def view_users(request):
    us = userr.objects.all()
    return render(request,'admin/details.html',{'use':us})

def deleteuser(request,pk):
    if request.user.is_authenticated:
        us = userr.objects.get(id=pk)
        usr = User.objects.get(username = us.user_name.username)
        us.delete()
        usr.delete()
        messages.success(request,'User Deleted Successfully')
        return redirect('view_users')


def footer_user(request):
    if request.user.is_authenticated:
        it = Item.objects.all()
        return render(request,'user/userfooter.html',{'ite':it})
    else:
        return render(request,'user/userfooter.html')    

   
def productuser(request, pk):
    if request.user.is_authenticated:
        it = Item.objects.all()
        
        it = Item.objects.get(id=pk)
        try:
            us = userr.objects.get(user_name=request.user)
        except userr.DoesNotExist:
            us = None
        pdt = Product.objects.filter(catname=it)
        return render(request, 'user/userproduct.html', {'pdt': pdt, 'ite': it, 'selected_category': pk,'use': us})
    

def all_products(request):
    if request.user.is_authenticated:   
        it= Item.objects.all()
        us = userr.objects.get(user_name=request.user)
        pdt = Product.objects.all()
        return render(request, 'user/product.html', {'pdt': pdt, 'ite': it, 'use': us})
    else:
        return redirect('/')



@login_required
def add_to_cart(request, pk):
    pro = Product.objects.get(id=pk)
    cart_item, created = Cart.objects.get_or_create(ucart=request.user,uproduct=pro)
    if not created:
        cart_item.quantity += 1
        cart_item.save()
    
    
    it = Item.objects.all()
    messages.success(request, 'Product Added To Cart')
    return redirect('cart_view')
    
    

def cart_remove(request, pk):   
    if request.user.is_authenticated:
        pro = Product.objects.get(id=pk)
        cart_item = Cart.objects.filter(ucart=request.user, uproduct=pro)
        if cart_item:
            cart_item.delete()
        return redirect('cart_view')    


def cart_view(request):
    if request.user.is_authenticated:
        cart_items = Cart.objects.filter(ucart=request.user).select_related('uproduct')
        total_price = sum(item.total_price() for item in cart_items)
        it = Item.objects.all()
        try:
            us = userr.objects.get(user_name=request.user)
        except userr.DoesNotExist:
            cust = None
        return render(request, 'user/productcart.html', {'cart': cart_items, 'total_price': total_price,'cust':cust,'ite':it})

def checkout(request):
    if request.user.is_authenticated:
        cart_items = Cart.objects.filter(ucart=request.user).select_related('uproduct')
        total_price = sum(item.total_price() for item in cart_items)
        crt = Cart.objects.filter(ucart=request.user)
        it = Item.objects.all()
        try:
            us = userr.objects.get(user_name=request.user)
        except userr.DoesNotExist:
            us = None
        return render(request, 'user/details.html', {'cart': cart_items, 'total_price': total_price,'cart':crt,'use':us,'ite':it})

def user_logout(request):
    auth.logout(request)
    return redirect('home') 

def decrement(request,pk):
    if request.user.is_authenticated:
        cart_item = Cart.objects.get(uproduct_id =pk, ucart=request.user)
        cart_item.quantity -= 1
        cart_item.save()
        return redirect('cart_view')

def increment(request,pk):  
    if request.user.is_authenticated:
        cart_item = Cart.objects.get(uproduct_id =pk, ucart=request.user)
        cart_item.quantity += 1
        cart_item.save()
        return redirect('cart_view')     

def checkout_process(request):
    return render(request,'user/final.html')
