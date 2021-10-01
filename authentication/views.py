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
                print('asdassssssssaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa', user.role , user.is_admin)
                op = user.role
                lk = str(op)
                # messages.success(request, f'You have been succesfully logged in!')
                if lk == "tyh":
                    print('asdassssssssaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa', valuenext, user.is_admin)
                    if valuenext:
                        return redirect(valuenext)
                    else:
                        return redirect('ad_create_account')

                # elif user.title == 'HR Officer' and user.is_admin==False:
                #     if valuenext:
                #         return redirect(valuenext)
                #     else:
                #         return redirect('human-resources-home')
                # elif user.title == 'Record Officer' and user.is_admin==False:
                #     if valuenext:
                #         return redirect(valuenext)
                #     else:
                #         return redirect('record-officer-home')
                # elif user.title == 'Team Leader' and user.is_admin==False:
                #     if valuenext:
                #         return redirect(valuenext)
                #     else:
                #         return redirect('team-leader-home')
                # elif user.title == 'Lead Engineer' and user.is_admin==False:
                #     if valuenext:
                #         return redirect(valuenext)
                #     else:
                #         return redirect('lead-engineer-home')
                # elif user.title == 'Project Engineer' and user.is_admin==False:
                #     if valuenext:
                #         return redirect(valuenext)
                #     else:
                #         return redirect('project-engineer-home')
        else:
            messages.warning(request, f'The Login Credentials you entered are not correct!')
    else:

    # messages.info(request, f'Welcome! You have to login to access further pages!')
        return render(request, 'authentication/index.html')


    # messages.info(request, f'Welcome! You have to login to access further pages!')
    



def logoutView(request):
    logout(request)
    return redirect('login_page')
