from django.shortcuts import render, redirect
from .forms import registrationForm
from .models import *
from django.template.context_processors import csrf
from django.contrib import messages
from django.contrib.auth.decorators import login_required, user_passes_test
from authentication.models import User

# Create your views here.



ad_login_required = user_passes_test(
    lambda user: True if user.role == "Assistant Director" and not user.is_admin else False, login_url='/')


def only_ad(view_func):
    decorated_view_func = login_required(
        ad_login_required(view_func), login_url='/')
    return decorated_view_func



# Create your views here.
@login_required
def index(request):
    context = {}
    
    context["data"] = User.objects.get(username = request.user.username)
    rol = request.user.role
    context["role"] = len(str(rol))
    return render(request, 'assistant_director/index.html', context)





@login_required
def registrationView(request):
    context = {}
    # context["data"] = User.objects.get(id = id)
    context["data"] = User.objects.get(username = request.user.username)
    context["lists"] = User.objects.filter(is_admin = False)
    if request.POST:
        form = registrationForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password1')
            # auth = authenticate(username=username, password=password)
            # login(request,auth)
            messages.success(request, f'The Account is succesfully created user { username } now has access!')
            
            return redirect('ad_manage_accounts')
        else:
            form = registrationForm(request.POST)
            context ["form"] = form
            return render(request, 'assistant_director/register_user.html', context)


    else:
        form = registrationForm()
        context ["form"] = form
    return render(request, 'assistant_director/register_user.html', context)





@login_required
def profile(request):
    context = {}
    context["data"] = User.objects.get(username = request.user.username)
    rol = request.user.role
    context["role"] = len(str(rol))
    return render(request, 'assistant_director/profile.html', context)




@login_required
def manageUsersView(request):
    context = {}
    # context["data"] = User.objects.get(id = id)
    context["data"] = User.objects.get(username = request.user.username)
    context["lists"] = User.objects.filter(is_admin = False)
    return render(request, 'assistant_director/manage_users.html', context)


