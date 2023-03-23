from django.shortcuts import render
from django.http import HttpResponse
from .models import *
from .forms import *
# Create your views here.

def home(request):
    cus=Customer.objects.all()
    orde=Order.objects.all()
    total_cus=cus.count()
    total_ord=orde.count()
    deliv=orde.filter(status='Delivered').count()
    pending=orde.filter(status='pending').count()
    
    context={'cus':cus,'orde':orde,'total_ord':total_ord,'total_cus':total_cus,
             'pending':pending,'delivered':deliv}
    
    return render(request,'accounts/dashboard.html',context)

def products(request):
    pro=Product.objects.all()
    return render(request,'accounts/products.html',{'prod':pro})

def customer(request,pk):
    cus=Customer.objects.get(id=pk)
    orde=cus.order_set.all()
    total_ord=orde.count()
    context={'cus':cus,'orde':orde,'total_ord':total_ord}
    return render(request,'accounts/customer.html',context)

def createOrder(request):
    form=OrderForm()
    context={'form':form}
    return render(request,'accounts/order_form.html',context)