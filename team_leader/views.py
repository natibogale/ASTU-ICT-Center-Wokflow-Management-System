from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404, redirect, render
from django.contrib import messages

from authentication.models import User
from director.forms import addProjectsForm
from director.models import  Projects
from .models import *
from .forms import *
import uuid


@login_required
def index(request):
    context = {}
    context["data"] = User.objects.get(username = request.user.username)
    rol = request.user.role
    context["role"] = len(str(rol))
    return render(request, 'team_leader/index.html', context)


@login_required
def profile(request):
    context = {}
    context["data"] = User.objects.get(username = request.user.username)
    rol = request.user.role
    context["role"] = len(str(rol))
    return render(request, 'team_leader/profile.html', context)



@login_required
def manageProjects(request):
    context = {}
    
    context["data"] = User.objects.get(username = request.user.username)
    rol = request.user.role
    context["role"] = len(str(rol))
    context["lists"] = Projects.objects.filter(is_active=True, assignedTeam=request.user.team).order_by('-dateAdded')
    if request.method == 'POST':
        print(request.method)
        form = addProjectsForm(request.POST, request.FILES)
        if form.is_valid():
            project = form.save(commit=False)
            project.created_by = request.user
            project.save()
            messages.success(request, f'New Project has been added!')
            return redirect ('tl_add_projects')
        else:
            form = addProjectsForm(request.POST, request.FILES)
            context["form"] = form
            return render(request, "team_leader/manage_projects.html", context)
    else:
        form = addProjectsForm()
        context["form"] = form

    return render(request, "team_leader/manage_projects.html", context)




@login_required
def assignExpert(request,id):
    obj = get_object_or_404(Projects, id = id)
    context = {}
    context["data"] = User.objects.get(username = request.user.username)
    rol = request.user.role
    context["role"] = len(str(rol))
    context["lists"] = Projects.objects.filter(is_active=True, assignedTeam=request.user.team).order_by('-dateAdded')
    if request.method == 'POST':
        print(request.method)
        form = assignExpertForm(request.POST, request.FILES, instance = obj)
        if form.is_valid():
            project = form.save(commit=False)
            project.expertUnique = uuid.uuid1()
            project.save()
            messages.success(request, f'Project has been assigned')
            return redirect ('tl_manage_projects')
        else:
            form = assignExpertForm(request.POST, request.FILES,  instance = obj)
            context["form"] = form
            return render(request, "team_leader/assign_expert.html", context)
    else:
        form = assignExpertForm(instance = obj)
        context["form"] = form

    return render(request, "team_leader/assign_expert.html", context)



@login_required
def messagesView(request,id,messageTo):
    obj = get_object_or_404(Projects, id = id)
    context = {}    
    context["data"] = User.objects.get(username = request.user.username)
    rol = request.user.role
    context["obj"] = obj
    context["role"] = len(str(rol))
    context["lists"] =  ExpertProjectMessages.objects.filter(projectUnique  = obj.expertUnique ) .order_by('sentDate')
    print('asssssssssssssssssssssssssssssss',context)
    if request.method == 'POST':
        print(request.method)
        form = sendMessagesForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, f'Message is sent')
            return redirect (request.META['HTTP_REFERER'])
        else:
            form = assignExpertForm(request.POST, request.FILES)
            context["form"] = form
            return render(request, "team_leader/project_messages.html", context)
    else:
        form = assignExpertForm()
        context["form"] = form

    return render(request, "team_leader/project_messages.html",context)