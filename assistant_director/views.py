from django.shortcuts import render, redirect
from .forms import registrationForm
from .models import *
from django.template.context_processors import csrf
from django.contrib import messages
from django.contrib.auth.decorators import login_required

# Create your views here.


# Create your views here.
def index(request):
    return render(request, 'assistant_director/index.html')

@login_required
def registrationView(request):
    if request.POST:
        form = registrationForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password1')
            # auth = authenticate(username=username, password=password)
            # login(request,auth)
            messages.success(request, f'The Account is succesfully created user { username } now has access!')
            return redirect('ad_create_account')
        # else:
        #     # form = registrationForm(request.POST, request.FILES)

    else:
        form = registrationForm()
    return render(request, 'assistant_director/index.html', { 'form' : form})