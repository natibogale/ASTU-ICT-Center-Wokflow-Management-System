from django.contrib.auth.decorators import login_required
from django.http.response import HttpResponseRedirect
from django.shortcuts import get_object_or_404, redirect, render
from django.contrib import messages

from authentication.models import User
from director.forms import addProjectsForm
from director.models import  Projects, TeamProjectMessages
from .models import *
from .forms import *
import uuid
from datetime import date


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
    context["date"] = date.today()
    # if request.method == 'POST':
    #     print(request.method)
    #     form = addProjectsForm(request.POST, request.FILES)
    #     if form.is_valid():
    #         project = form.save(commit=False)
    #         project.created_by = request.user
    #         project.save()
    #         messages.success(request, f'New Project has been added!')
    #         return redirect ('tl_add_projects')
    #     else:
    #         form = addProjectsForm(request.POST, request.FILES)
    #         context["form"] = form
    #         return render(request, "team_leader/manage_projects.html", context)
    # else:
    #     form = addProjectsForm()
    #     context["form"] = form

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
            pr = form.cleaned_data["assignedExpert"]
            usr = User.objects.get(id = pr.id )
            project.currentlyOn = usr.firstName + ' ' + usr.lastName 
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
    context["lists"] =  ExpertProjectMessages.objects.filter(projectUnique  = obj.expertUnique ).order_by('sentDate')
    if request.method == 'POST':
        print(request.method)
        form = sendMessagesForm(request.POST, request.FILES)
        if form.is_valid():
            message = form.save(commit=False)
            message.messageSender = request.user
            message.messageTo = obj.assignedExpert
            message.projectId = obj
            message.projectUnique = obj
            message.save()
            messages.success(request, f'Message is sent')
            form = sendMessagesForm(None)
            context["form"] = form
            return HttpResponseRedirect("/team-leader/project-messages/"+ str(message.projectId.id) + "/" + message.messageTo.username ) 
            # render(request, "team_leader/project_messages.html", context)
        else:
            form = sendMessagesForm(request.POST, request.FILES)
            context["form"] = form
            return render(request, "team_leader/project_messages.html", context)
    else:
        form = sendMessagesForm()
        context["form"] = form

    return render(request, "team_leader/project_messages.html",context)







@login_required
def teamMessagesView(request,id,messageTo):
    obj = get_object_or_404(Projects, id = id)
    context = {}    
    context["data"] = User.objects.get(username = request.user.username)
    rol = request.user.role
    context["obj"] = obj
    context["role"] = len(str(rol))
    context["lists"] =  TeamProjectMessages.objects.filter(projectUnique  = obj.teamUnique ).order_by('sentDate')
    if request.method == 'POST':
        print(request.method)
        form = teamSendMessagesForm(request.POST, request.FILES)
        if form.is_valid():
            message = form.save(commit=False)
            message.messageSender = request.user
            message.messageTo = obj.assignedExpert
            message.projectId = obj
            message.projectUnique = obj
            message.save()
            messages.success(request, f'Message is sent')
            form = sendMessagesForm()
            context["form"] = form
            return HttpResponseRedirect("/team-leader/team-project-messages/"+ str(message.projectId.id) + "/" + message.messageTo.username ) 
        else:
            form = teamSendMessagesForm(request.POST, request.FILES)
            context["form"] = form
            return render(request, "team_leader/team_project_messages.html", context)
    else:
        form = teamSendMessagesForm()
        context["form"] = form

    return render(request, "team_leader/team_project_messages.html",context)
