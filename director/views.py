from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect, render
from django.contrib import messages

from authentication.models import User
from .forms import *

# Create your views here.


@login_required
def index(request):
    context = {}
    
    context["data"] = User.objects.get(username = request.user.username)
    rol = request.user.role
    context["role"] = len(str(rol))
    return render(request, 'director/index.html', context)



@login_required
def profile(request):
    context = {}
    context["data"] = User.objects.get(username = request.user.username)
    rol = request.user.role
    context["role"] = len(str(rol))
    return render(request, 'director/profile.html', context)


@login_required
def addProjects(request):
    context = {}
    context["data"] = User.objects.get(username = request.user.username)
    rol = request.user.role
    context["role"] = len(str(rol))

    if request.method == 'POST':
        print(request.method)
        form = addProjectsForm(request.POST, request.FILES)
        if form.is_valid():
            project = form.save(commit=False)
            project.created_by = request.user
            project.save()
            messages.success(request, f'New Project has been added!')
            return redirect ('dr_manage_projects')
        else:
            form = addProjectsForm(request.POST, request.FILES)
            context["form"] = form
            return render(request, "director/add_projects.html", context)
    else:
        form = addProjectsForm()
        context["form"] = form

    return render(request, "director/add_projects.html", context)



@login_required
def manageProjects(request):
    context = {}
    context["data"] = User.objects.get(username = request.user.username)
    rol = request.user.role
    context["role"] = len(str(rol))
    context["lists"] = Projects.objects.filter(is_active=True).order_by('-dateAdded')

    return render(request, "director/manage_projects.html", context)