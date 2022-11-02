# Create your views here.
from cProfile import Profile
from http.client import HTTPResponse
from django.contrib import messages
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required

from django.shortcuts import redirect, render, get_object_or_404
from django.core.paginator import Paginator
from django.conf import settings

from users.filters import ProfileFilter

from .forms import LoginForm, OrderForm, CreateProfileForm, EditProfileForm, CreateUserForm
from .models import Friend_Request


@login_required
def send_friend_request(request, userID):
    from_user = request.user
    to_user = settings.AUTH_USER_MODEL.objects.get(id=userID)
    friend_request, created = Friend_Request.objects.get_or_create(
        from_user= from_user, to_user=to_user
    )
    if created:
        return HTTPResponse("friend request send")
    else:
        return HTTPResponse("friend request was already sent")

@login_required
def accept_friend_request(request, requestID):
    friend_request = Friend_Request.objects.get(id=requestID)
    if friend_request.to_user == request.user:
        friend_request.to_user.friends.add(friend_request.from_user)
        friend_request.from_user.friends.add(friend_request.to_user)
        friend_request.delete()
        return HTTPResponse("friend request accepted")
    else:
        return HTTPResponse("friend request not accepted")

@login_required
def dashboard(request):
    return render(request, 'social/dashboard.html', {'dashboard':'dashboard'})


def redirect_after_login(request):
    nxt = request.GET.get("next", None)
    if nxt is None:
        return redirect(settings.LOGIN_REDIRECT_URL)    
    else:
        return redirect(nxt)

def profile_list(request):
    story_list = Profile.objects.order_by('name')
    story_filter = ProfileFilter(request.GET, queryset=story_list)

    paginator = Paginator(story_filter.qs, 2)

    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    context = { "page_obj": page_obj, "filter": story_filter, 'value':'profiles'}

    return render(request, "views/profiles.html", context)


def profile_detail_view(request):   
    story_filter = ProfileFilter(request.GET, queryset=Profile.objects.all())
    context_404 = { "data": get_object_or_404(Profile,id=id), "filter": story_filter,}
    return render(request, "views/profile_detail_view.html", context_404)

       
def profile_update_view(request, id):
    context = {}
    obj = get_object_or_404(Profile,id=id)
    form = EditProfileForm(request.POST or None, instance=obj)
    if form.is_valid():
        form.save()
        try:
            return redirect('/users/profile/'+id)
        except:
            pass
    context['form'] = form
    return render(request, "views/profile_update_view.html", context)

def profile_delete_view(request, id):
    context = {}
    obj = get_object_or_404(Profile,id=id)
    form = EditProfileForm(request.POST or None, instance=obj)
    if request.method=="POST":
        obj.delete()
        try:
            return redirect('/users/profiles')
        except:
            pass
    context['form'] = form
    return render(request, "views/profile_delete_view.html", context)

def user_login(request):
    if request.method == "POST":
        form = LoginForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            user = authenticate(request, username = cd['username'], password=cd['password'])
            if user is not None:
                if user.is_active:
                    login(request, user)
                    messages.info(request,'Authenticated successfully')
                    return redirect_after_login(request)
                else:
                    messages.info(request,'Disabled account')  
                    return redirect_after_login(request)

            else:
                messages.info(request,'Invalid account')
                return redirect_after_login(request)

    else:
        form = LoginForm()
    return render(request, 'social/login.html', {'form':form})

def register(request):
    if request.method == "POST":
        user_form = CreateUserForm(request.POST)
        if user_form.is_valid():
            new_user = user_form.save(commit=False)
            new_user.set_password(user_form.cleaned_data['password'])
            new_user.save()
            return redirect_after_login(request)
    else:
        user_form = CreateUserForm()
    return render(request, 'social/register.html', {'user_form':user_form})


def user_logout(request):
    logout(request)
    return redirect('home')

def users_list(request):
    story_list = Profile.objects.order_by('name')
    story_filter = ProfileFilter(request.GET, queryset=story_list)

    paginator = Paginator(story_filter.qs, 2)

    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    context = { "page_obj": page_obj, "filter": story_filter, 'value':'users'}

    return render(request, "views/profiles.html", context)


def order(request):
    if request.method == "POST":
        user_form = OrderForm(request.POST or None)
        if user_form.is_valid():
            # new_user = user_form.save(commit=False)
            user_form.save()
            try:
                return redirect('books')
            except:
                pass
        context = {
            'form': user_form,
        }
        return render(request, "index.html", context)