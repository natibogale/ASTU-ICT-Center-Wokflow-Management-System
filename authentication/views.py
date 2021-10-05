from django.shortcuts import render, redirect,HttpResponse
from .forms import *
# Create your views here.
from django.contrib.auth import *
from .models import *
from django.contrib import messages

def home(request):
    # user = request.user
    # if user.is_authenticated:
    #     return redirect('record-officer-home')

    if request.method == 'POST':
        form = loginForm(request.POST)
        if form.is_valid():
            username = request.POST['username']
            password = request.POST['password']
            user = authenticate(username=username , password=password)
            if user and user.is_admin==False:
                login(request, user)
                valuenext= request.POST.get('next')
                op = user.role
                lk = str(op)
                # messages.success(request, f'You have been succesfully logged in!')
                if lk == "Assistant Director":
                    if valuenext:
                        print("sdfsdfsdfsdfsdfsdfsdfsdfsdfsdfsdfsdfsdfsdf")
                        return redirect(valuenext)
                    else:
                        return redirect('ad_home_page') 

                elif lk == 'ICT Director':
                    if valuenext:
                        return redirect(valuenext)
                    else:
                        return redirect('dr_home_page')
                elif lk == 'Team Leader':
                    if valuenext:
                        return redirect(valuenext)
                    else:
                        return redirect('tl_home_page')
                elif lk == 'Expert':
                    if valuenext:
                        return redirect(valuenext)
                    else:
                        return redirect('exp_home_page')
        else:
            messages.warning(request, f'The Login Credentials you entered are not correct!')
            return render(request, 'authentication/index.html')

    else:

    # messages.info(request, f'Welcome! You have to login to access further pages!')
        return render(request, 'authentication/index.html')
    # messages.info(request, f'Welcome! You have to login to access further pages!')
    

def logoutView(request):
    logout(request)
    return redirect('login_page')
