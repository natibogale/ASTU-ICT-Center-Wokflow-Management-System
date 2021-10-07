from django.contrib.auth.decorators import login_required
from django.http.response import HttpResponseRedirect
from django.shortcuts import get_object_or_404, redirect, render
from django.contrib import messages

from authentication.models import User
from .forms import *
from datetime import date
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
            team = form.cleaned_data["assignedTeam"]
            usr = User.objects.get(team = team , role = 3 )
            project.currentlyOn = usr.firstName + ' ' + usr.lastName 
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
    context["date"] = date.today()
    context["lists"] = Projects.objects.filter(is_active=True).order_by('-dateAdded')

    return render(request, "director/manage_projects.html", context)



@login_required
def messagesView(request,id,messageTo):
    obj = get_object_or_404(Projects, id = id)
    context = {}    
    context["data"] = User.objects.get(username = request.user.username)
    rol = request.user.role
    context["obj"] = obj
    context["role"] = len(str(rol))
    context["lists"] =  TeamProjectMessages.objects.filter(projectUnique  = obj.teamUnique ).order_by('sentDate')
    if request.method == 'POST':

        if request.POST["submit"] == 'Approve Project':
            form2 = directorApproveForm(request.POST, instance=obj)
            if form2.is_valid():
                obj.currentlyOn = request.user.firstName + " " + request.user.lastName
                obj.is_active = False
                obj.directorApprovedDate = date.today()
                if obj.deadLine < date.today():
                    obj.is_late = True
                form2 = directorApproveForm(request.POST, instance=obj)
                form2.save() 
                messages.success(request, f'Project is approved from Team Leader')
                return HttpResponseRedirect("/director/project-messages/"+ str(obj.id) + "/" + messageTo ) 
            else:
                form = sendMessagesForm()
                context["form"] = form
                form2 = directorApproveForm()
                context["form2"] = form2
                return render(request, "director/project_messages.html", context)
        elif  request.POST["submit"] == 'Send Message':
            print(request.method)
            form = sendMessagesForm(request.POST, request.FILES)
            if form.is_valid():
                message = form.save(commit=False)
                message.messageSender = request.user
                to = User.objects.get(team = obj.assignedTeam, role=3)
                message.messageTo = to
                message.projectId = obj
                message.projectUnique = obj
                message.save()
                messages.success(request, f'Message is sent')
                form = sendMessagesForm()
                context["form"] = form
                return HttpResponseRedirect("/director/project-messages/"+ str(message.projectId.id) + "/" + message.messageTo.username ) 
            else:
                form = sendMessagesForm(request.POST, request.FILES)
                context["form"] = form
                form2 = directorApproveForm()
                context["form2"] = form2
                return render(request, "director/project_messages.html", context)
    else:
        form = sendMessagesForm()
        context["form"] = form
        form2 = directorApproveForm()
        context["form2"] = form2

    return render(request, "director/project_messages.html",context)





@login_required
def projectsArchive(request):
    context = {}
    context["data"] = User.objects.get(username = request.user.username)
    rol = request.user.role
    context["role"] = len(str(rol))
    context["date"] = date.today()
    context["lists"] = Projects.objects.all().order_by('-dateAdded')

    return render(request, "director/projects_archive.html", context)



@login_required
def projectDetail(request,id):
    context = {}
    context["data"] = User.objects.get(username = request.user.username)
    rol = request.user.role
    context["role"] = len(str(rol))
    context["date"] = date.today()
    obj = Projects.objects.get(id=id)
    form = projectDetailForm(instance=obj)
    context["form"] = form
    context["obj"] = obj
    if request.method == 'POST':
        print(request.method)
        form = projectDetailForm(request.POST or None,request.FILES or None, instance=obj)
        if form.is_valid():
            project = form.save(commit=False)
            team = form.cleaned_data["assignedTeam"]
            usr = User.objects.get(team = team , role = 3 )
            project.currentlyOn = usr.firstName + ' ' + usr.lastName 
            project.save()
            messages.success(request, f'Project has been Updated!')
            return HttpResponseRedirect("/director/project-detail/"+ str(id)  ) 

        else:
            form = projectDetailForm(request.POST or None,
                                 request.FILES or None, instance=obj)
            context["form"] = form
            return render(request, "director/project_detail.html", context)
    else:
        form = projectDetailForm(instance=obj)
        context["form"] = form

    return render(request, "director/project_detail.html", context)