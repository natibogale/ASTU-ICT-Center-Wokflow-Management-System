from django.contrib.auth.decorators import login_required
from django.db.models.query_utils import Q
from django.http.response import HttpResponseRedirect
from django.shortcuts import get_object_or_404, redirect, render
from django.contrib import messages

from authentication.models import User
from director.forms import addProjectsForm, profileDetail
from director.models import  Projects, Reports, TeamProjectMessages
from team_leader.forms import sendMessagesForm, teamReportMessagesForm
from team_leader.models import ExpertProjectMessages, TeamMessages
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




@login_required
def manageReports(request):
    context = {}
    context["data"] = User.objects.get(username = request.user.username)
    rol = request.user.role
    context["role"] = len(str(rol))
    context["date"] = date.today()
    context["lists"] = Reports.objects.filter(is_active=True).order_by('-dateAdded')
    return render(request, "experts/manage_reports.html", context)





@login_required
def reportDetail(request,id):
    context = {}
    context["data"] = User.objects.get(username = request.user.username)
    rol = request.user.role
    context["role"] = len(str(rol))
    context["date"] = date.today()
    obj = Reports.objects.get(id=id)
    form = reportDetailForm(instance=obj)
    context["form"] = form
    context["obj"] = obj
    context["teams"] = Teams.objects.exclude(teamName = 'All')
    form = reportDetailForm(instance=obj)
    context["form"] = form

    return render(request, "experts/report_detail.html", context)




@login_required
def reportsArchive(request):
    context = {}
    context["data"] = User.objects.get(username = request.user.username)
    rol = request.user.role
    context["role"] = len(str(rol))
    context["date"] = date.today()
    context["lists"] = Reports.objects.all().order_by('-dateAdded')
    return render(request, "experts/reports_archive.html", context)





@login_required
def teamReportMessagesView(request,id):
    obj = get_object_or_404(Reports, id = id)
    context = {}    
    context["data"] = User.objects.get(username = request.user.username)
    rol = request.user.role
    context["obj"] = obj
    context["role"] = len(str(rol))
    context["team"] = request.user.team
    messageTo = request.user.team
    acv = Teams.objects.get(id = messageTo.id)
    context["lists"] =  TeamMessages.objects.filter(Q(reportId = id), Q(messageTo = messageTo.id)).order_by('sentDate')
    if request.method == 'POST':
        print(request.method)
        form = teamReportMessagesForm(request.POST, request.FILES)
        if form.is_valid():
            message = form.save(commit=False)
            message.messageSender = request.user
            team = Teams.objects.get(id=messageTo.id)
            message.messageTo = team
            message.reportId = obj
            message.save()
            messages.success(request, f'Message is sent')
            form = teamReportMessagesForm()
            context["form"] = form
            return HttpResponseRedirect("/experts/team-report-messages/"+ str(message.reportId.id) ) 
        else:
            form = teamReportMessagesForm(request.POST, request.FILES)
            context["form"] = form
            return render(request, "experts/team_report_messages.html", context)
    else:
        form = teamReportMessagesForm()
        context["form"] = form


    return render(request, "experts/team_report_messages.html",context)


