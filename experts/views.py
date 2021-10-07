from django.contrib.auth.decorators import login_required
from django.http.response import HttpResponseRedirect
from django.shortcuts import get_object_or_404, redirect, render
from django.contrib import messages

from authentication.models import User
from director.forms import addProjectsForm, profileDetail
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
    obj = User.objects.get(username = request.user.username)
    rol = request.user.role

    context["role"] = len(str(rol))
    if request.method == 'POST':
        form = profileDetail(request.POST or None,
                                 request.FILES or None, instance=obj)
        if form.is_valid():
            ref = form.cleaned_data["username"]
            form.save()
            messages.success(
                request, f'"{ ref }"   your profile has been updated!')

            return redirect('exp_profile')

        else:
            context["form"] = form
            return render(request, 'experts/profile.html', context)

    else:
        form = profileDetail(instance=obj)
        context["form"] = form

    return render(request, 'experts/profile.html', context)




@login_required
def manageProjects(request):
    context = {}
    
    context["data"] = User.objects.get(username = request.user.username)
    rol = request.user.role
    context["role"] = len(str(rol))
    context["lists"] = Projects.objects.filter(is_active=True, assignedTeam=request.user.team, assignToExperts = True ).order_by('-dateAdded')
    context["date"] = date.today()
    return render(request, "experts/manage_projects.html", context)




@login_required
def expertMessagesView(request,id):
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
            message.messageTo = "Team Leader"
            message.projectId = obj
            message.projectUnique = obj
            message.save()
            messages.success(request, f'Message is sent')
            form = sendMessagesForm(None)
            context["form"] = form
            return HttpResponseRedirect("/experts/project-messages/"+ str(message.projectId.id)  ) 
            # render(request, "team_leader/project_messages.html", context)
        else:
            form = sendMessagesForm(request.POST, request.FILES)
            context["form"] = form
            return render(request, "experts/project_messages.html", context)
    else:
        form = sendMessagesForm()
        context["form"] = form

    return render(request, "experts/project_messages.html",context)







@login_required
def projectsArchive(request):
    context = {}
    context["data"] = User.objects.get(username = request.user.username)
    rol = request.user.role
    context["role"] = len(str(rol))
    context["date"] = date.today()
    context["lists"] = Projects.objects.filter(assignedTeam = request.user.team, assignToExperts = True ).order_by('-dateAdded')
    return render(request, "experts/projects_archive.html", context)







@login_required
def projectDetail(request,id):
    context = {}
    context["data"] = User.objects.get(username = request.user.username)
    rol = request.user.role
    context["role"] = len(str(rol))
    context["date"] = date.today()
    obj = Projects.objects.get(id=id)
    form = expertProjectDetailForm(instance=obj)
    context["form"] = form
    context["obj"] = obj
    
    return render(request, "experts/project_detail.html", context)
