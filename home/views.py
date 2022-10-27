from django.http import HttpResponse
from django.template import loader
from django.shortcuts import redirect, render, get_object_or_404
from users.forms import OrderForm

from users.models import Filter, Gallery, Navbar, Order, Pricing, Profile, Service, Social, Counter, Testimonial
from .models import GeeksModel
from .forms import GeeksForm


def home(request):
    context = {"data": Profile.objects.filter(user=1), "filters": Filter.objects.all(), 
    "service": Service.objects.all(), "gallery": Gallery.objects.all(),
    "socials": Social.objects.filter(user=1), "pricing": Pricing.objects.all(),
    "navbar": Navbar.objects.filter(user=1), "counter": Counter.objects.all(),
    "testimonial": Testimonial.objects.all(),
    }    
    return render(request, "homecopy.html", context)

def pricing_detail_view(request, id):
    context = {"pricing": Pricing.objects.get(id=id), "form": OrderForm()}
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
    context = { "dataset": Order.objects.all()}
    return render(request, "views/orders.html", context)

def orders_complete(request, id):
    context = {}
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

def info(request):
    context = { "dataset": GeeksModel.objects.all()}
    return render(request, "info.html", context)


def profiles(request):
    context = { "dataset": GeeksModel.objects.all()}
    return render(request, "profiles.html", context)


def create_view(request):
    context = {}
    form = GeeksForm(request.POST or None)
    if form.is_valid():
        form.save()
        try:
            return redirect('/crud/list/')
        except:
            pass
    context['form'] = form
    return render(request, "views/create_view.html", context)

def list_view(request):
    context = { "dataset": GeeksModel.objects.all()}
    return render(request, "views/list_view.html", context)

def detail_view(request, id):
    context_404 = { "data": get_object_or_404(GeeksModel,id=id)}
    return render(request, "views/detail_view.html", context_404)

def update_view(request, id):
    context = {}
    obj = get_object_or_404(GeeksModel,id=id)
    form = GeeksForm(request.POST or None, instance=obj)
    if form.is_valid():
        form.save()
        try:
            return redirect('/crud/list/'+id)
        except:
            pass
    context['form'] = form
    return render(request, "views/update_view.html", context)

def delete_view(request, id):
    context = {}
    obj = get_object_or_404(GeeksModel,id=id)
    form = GeeksForm(request.POST or None, instance=obj)
    if request.method=="POST":
        obj.delete()
        try:
            return redirect('/crud/list/')
        except:
            pass
    context['form'] = form
    return render(request, "views/delete_view.html", context)
