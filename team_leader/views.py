from django.contrib.auth.decorators import login_required
from django.http.response import HttpResponseRedirect
from django.shortcuts import get_object_or_404, redirect, render
from django.contrib import messages

from authentication.models import User
from director.forms import addProjectsForm, profileDetail
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

            return redirect('tl_profile')

        else:
            context["form"] = form
            return render(request, 'team_leader/profile.html', context)

    else:
        form = profileDetail(instance=obj)
        context["form"] = form

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
            project.currentlyOn = "Experts"
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
def messagesView(request,id):
    obj = get_object_or_404(Projects, id = id)
    context = {}    
    context["data"] = User.objects.get(username = request.user.username)
    rol = request.user.role
    context["obj"] = obj
    context["role"] = len(str(rol))
    context["lists"] =  ExpertProjectMessages.objects.filter(projectUnique  = obj.expertUnique ).order_by('sentDate')
    if request.method == 'POST':
        if request.POST["submit"] == 'Approve Project':
            form2 = leaderApproveForm(request.POST, instance=obj)
            if form2.is_valid():
                obj.currentlyOn = request.user.firstName + " " + request.user.lastName
                obj.leaderApprovedDate = date.today()
                form2 = leaderApproveForm(request.POST, instance=obj)
                form2.save() 
                messages.success(request, f'Project is approved from expert')
                return HttpResponseRedirect("/team-leader/project-messages/"+ str(obj.id)  ) 
            else:
                form = sendMessagesForm()
                context["form"] = form
                form2 = leaderApproveForm()
                context["form2"] = form2
                return render(request, "team_leader/project_messages.html", context)
        elif  request.POST["submit"] == 'Send Message':
            print(request.method)
            form = sendMessagesForm(request.POST, request.FILES)
            if form.is_valid():
                message = form.save(commit=False)
                message.messageSender = request.user
                message.projectId = obj
                message.messageTo = "Experts"
                message.projectUnique = obj
                message.save()
                messages.success(request, f'Message is sent')
                form = sendMessagesForm(None)
                context["form"] = form
                return HttpResponseRedirect("/team-leader/project-messages/"+ str(message.projectId.id) ) 
                # render(request, "team_leader/project_messages.html", context)
            else:
                form = sendMessagesForm(request.POST, request.FILES)
                context["form"] = form
                form2 = leaderApproveForm()
                context["form2"] = form2
                return render(request, "team_leader/project_messages.html", context)
    else:
        form = sendMessagesForm()
        context["form"] = form

        form2 = leaderApproveForm()
        context["form2"] = form2


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
            message.messageTo = obj.created_by  
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




@login_required
def projectsArchive(request):
    context = {}
    context["data"] = User.objects.get(username = request.user.username)
    rol = request.user.role
    context["role"] = len(str(rol))
    context["date"] = date.today()
    context["lists"] = Projects.objects.filter(assignedTeam = request.user.team ).order_by('-dateAdded')
    return render(request, "team_leader/projects_archive.html", context)







@login_required
def projectDetail(request,id):
    context = {}
    context["data"] = User.objects.get(username = request.user.username)
    rol = request.user.role
    context["role"] = len(str(rol))
    context["date"] = date.today()
    obj = Projects.objects.get(id=id)
    form = teamProjectDetailForm(instance=obj)
    context["form"] = form
    context["obj"] = obj
    


    if request.method == 'POST':        
        print(request.method)
        form = teamProjectDetailForm(request.POST or None,request.FILES or None, instance=obj)
        print('aaaaaaaaaaaaaaaaaaaaaaa',form.is_valid(),form)

        if form.is_valid():
            print('aaaaaaaaaaaaaaaaaaaaaaa',form.is_valid())
            project = form.save(commit=False)
            team = form.cleaned_data["assignToExperts"]
            usr = User.objects.get(team = request.user.team , role = 4 )
            project.currentlyOn = usr.firstName + ' ' + usr.lastName 
            project.save()
            messages.success(request, f'Project has been Updated!')
            return HttpResponseRedirect("/team-leader/project-detail/"+ str(id)  ) 

        else:
            form = teamProjectDetailForm(request.POST or None,
                                request.FILES or None, instance=obj)
            context["form"] = form
            return render(request, "team_leader/project_detail.html", context)
    else:
        form = teamProjectDetailForm(instance=obj)
        context["form"] = form

    return render(request, "team_leader/project_detail.html", context)
