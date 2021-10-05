from django.contrib.auth.decorators import login_required
from django.http.response import HttpResponseRedirect
from django.shortcuts import get_object_or_404, redirect, render
from django.contrib import messages

from authentication.models import User
from director.forms import addProjectsForm
from director.models import  Projects, TeamProjectMessages
from team_leader.forms import sendMessagesForm
from team_leader.models import ExpertProjectMessages
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
    return render(request, 'experts/index.html', context)





@login_required
def profile(request):
    context = {}
    context["data"] = User.objects.get(username = request.user.username)
    rol = request.user.role
    context["role"] = len(str(rol))
    return render(request, 'experts/profile.html', context)




@login_required
def manageProjects(request):
    context = {}
    
    context["data"] = User.objects.get(username = request.user.username)
    rol = request.user.role
    context["role"] = len(str(rol))
    context["lists"] = Projects.objects.filter(is_active=True, assignedTeam=request.user.team, assignedExpert = request.user ).order_by('-dateAdded')
    context["date"] = date.today()
    return render(request, "experts/manage_projects.html", context)




@login_required
def expertMessagesView(request,id,messageTo):
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
            return HttpResponseRedirect("/experts/project-messages/"+ str(message.projectId.id) + "/" + message.messageTo.username ) 
            # render(request, "team_leader/project_messages.html", context)
        else:
            form = sendMessagesForm(request.POST, request.FILES)
            context["form"] = form
            return render(request, "experts/project_messages.html", context)
    else:
        form = sendMessagesForm()
        context["form"] = form

    return render(request, "experts/project_messages.html",context)
