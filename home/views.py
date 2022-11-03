from django.http import HttpResponse
from django.template import loader
from django.shortcuts import redirect, render, get_object_or_404
from users.forms import OrderForm

from users.models import Filter, Order, Profile, Social
from navbars.models import About, Gallery, Service, Counter, Testimonial, Pricing
from firsts.models import Navbar
from styling.models import ImageAnimation, Footer, Nav, Header

def home(request):
    context = {"data": Profile.objects.filter(user=1), "filters": Filter.objects.all(), 
    "service": Service.objects.all(), "gallery": Gallery.objects.all(),
    "socials": Social.objects.filter(user=1), "pricing": Pricing.objects.all(),
    "navbar": Navbar.objects.filter(user=1).order_by('order'), "counter": Counter.objects.all(),
    "testimonial": Testimonial.objects.all(), "about": About.objects.all(), "ia": ImageAnimation.objects.all(),
    "footer": Footer.objects.filter(id=1), "nav": Nav.objects.filter(id=1), "header": Header.objects.filter(id=1)
    }    
    return render(request, "home.html", context)

def pricing_detail_view(request, id):
    context = {
        "data": Profile.objects.filter(user=1),"pricing": Pricing.objects.get(id=id), "form": OrderForm(),
        "socials": Social.objects.filter(user=1),"footer": Footer.objects.filter(id=1), "nav": Nav.objects.filter(id=1)
    }
    pricing =  Pricing.objects.get(id=id)
    if request.method == "POST":
        form = OrderForm(request.POST or None)
        if form.is_valid():
            # new_user = user_form.save(commit=False)
            form.instance.price = pricing.price
            form.instance.name = pricing.name
            form.instance.title = pricing.title

            form.instance.item_quantity = pricing.item_quantity
            form.instance.item_amount = pricing.item_amount
            form.instance.item_name = pricing.item_name

            # form.instance.price = pricing.price
            form.save()
            try:
                return redirect('home')
            except:
                pass
    return render(request, "pricingform.html", context)

def orders(request):
    context = { 
        "data": Profile.objects.filter(user=1),"dataset": Order.objects.all(),
        "socials": Social.objects.filter(user=1),"footer": Footer.objects.filter(id=1), "nav": Nav.objects.filter(id=1)
        
    }
    return render(request, "views/orders.html", context)

def orders_complete(request, id):
    context = {
        "data": Profile.objects.filter(user=1), "form": OrderForm(),
        "socials": Social.objects.filter(user=1),"footer": Footer.objects.filter(id=1), "nav": Nav.objects.filter(id=1)
    }
    obj = get_object_or_404(Order,id=id)
    form = OrderForm(request.POST or None, instance=obj)
    if request.method=="POST":
        obj.delete()
        try:
            return redirect('orders')
        except: 
            pass
    context['form'] = form
    return render(request, "views/orders_complete.html", context)
