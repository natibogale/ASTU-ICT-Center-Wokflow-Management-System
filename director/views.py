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
    context["projects"] = Projects.objects.all().order_by('-dateAdded')
    context["data"] = User.objects.get(username = request.user.username)
    context["today"] = date.today()
    print('AAAAAAAAAaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa')
    rol = request.user.role
    context["role"] = len(str(rol))
    return render(request, 'director/index.html', context)



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

            return redirect('dr_profile')

        else:
            context["form"] = form
            return render(request, 'director/profile.html', context)

    else:
        form = profileDetail(instance=obj)
        context["form"] = form

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
        if request.POST["submit"] == 'Delete Project':
            obj = get_object_or_404(Projects, id = id)
            dire = Projects.objects.filter(created_by = request.user.id)
            if obj in dire:
                obj.delete()
                messages.success(request, f'Project    "{ obj }"   has been deleted!')
                return redirect('dr_manage_projects')
            else:
                messages.warning(request, f'Project    "{ obj }"   no longer exists !')
                return redirect('dr_manage_projects')

        elif request.POST["submit"] == 'Update Project':
            print(request.method)
            form = projectDetailForm(request.POST or None,request.FILES or None, instance=obj)
            print('aaaaaaaaaaaaaaaaaaaaaaa',form.is_valid(),form)

            if form.is_valid():
                team = form.cleaned_data["assignedTeam"]
                usr = User.objects.get(team = team , role = 3 )
                obj.currentlyOn = usr.firstName + ' ' + usr.lastName 
                if form.cleaned_data["directorApproved"] == True:
                    obj.directorApprovedDate = date.today()
                form = projectDetailForm(request.POST or None,request.FILES or None, instance=obj)
                form.save()
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



@login_required
def projectsDelete(request, id):
    obj = get_object_or_404(Projects, id = id)
    dire = Projects.objects.filter(directorate = request.user.directorate)
    if obj in dire:
        obj.delete()
        messages.success(request, f'Project    "{ obj }"   has been deleted!')
        return redirect('dr-manage-projects')
    else:
        return redirect('dr-manage-projects')






@login_required
def addReports(request):
    context = {}
    context["data"] = User.objects.get(username = request.user.username)
    rol = request.user.role
    context["role"] = len(str(rol))

    if request.method == 'POST':
        print(request.method)
        form = requestReportsForm(request.POST, request.FILES)
        if form.is_valid():
            report = form.save(commit=False)
            report.created_by = request.user
            report.save()
            messages.success(request, f'New Report has been requested!')
            return redirect ('dr_manage_reports')
        else:
            form = requestReportsForm(request.POST, request.FILES)
            context["form"] = form
            return render(request, "director/add_reports.html", context)
    else:
        form = requestReportsForm()
        context["form"] = form

    return render(request, "director/add_reports.html", context)




@login_required
def manageReports(request):
    context = {}
    context["data"] = User.objects.get(username = request.user.username)
    rol = request.user.role
    context["role"] = len(str(rol))
    context["date"] = date.today()
    context["lists"] = Reports.objects.filter(is_active=True).order_by('-dateAdded')
    return render(request, "director/manage_reports.html", context)







@login_required
def reportMessagesView(request,id):
    obj = get_object_or_404(Reports, id = id)
    context = {}    
    context["data"] = User.objects.get(username = request.user.username)
    rol = request.user.role
    context["obj"] = obj
    context["role"] = len(str(rol))
    context["lists"] =  DirectorReportMessages.objects.filter( reportId = id).order_by('sentDate')
    if request.method == 'POST':
        if request.POST["submit"] == 'Approve Report':
            form2 = directorReportApproveForm(request.POST, instance=obj)
            if form2.is_valid():
                obj.currentlyOn = request.user.firstName + " " + request.user.lastName
                obj.is_active = False
                obj.directorApprovedDate = date.today()
                if obj.deadLine < date.today():
                    obj.is_late = True
                form2 = directorReportApproveForm(request.POST, instance=obj)
                form2.save() 
                messages.success(request, f'Report is approved from Team Leader')
                return HttpResponseRedirect("/director/report-messages/"+ str(obj.id)  ) 
            else:
                form = reportSendMessagesForm()
                context["form"] = form
                form2 = directorReportApproveForm()
                context["form2"] = form2
                return render(request, "director/report_messages.html", context)
        elif  request.POST["submit"] == 'Send Message':
            print(request.method)
            form = reportSendMessagesForm(request.POST, request.FILES)
            if form.is_valid():
                message = form.save(commit=False)
                message.messageSender = request.user
                to = User.objects.get(role=2)
                message.messageTo = to
                message.reportId = obj
                message.save()
                messages.success(request, f'Message is sent')
                form = reportSendMessagesForm()
                context["form"] = form
                return HttpResponseRedirect("/director/report-messages/"+ str(message.reportId.id) ) 
            else:
                form = reportSendMessagesForm(request.POST, request.FILES)
                context["form"] = form
                form2 = directorApproveForm()
                context["form2"] = form2
                return render(request, "director/report_messages.html", context)
    else:
        form = reportSendMessagesForm()
        context["form"] = form
        form2 = directorReportApproveForm()
        context["form2"] = form2

    return render(request, "director/report_messages.html",context)







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
    if request.method == 'POST':
        if request.POST["submit"] == 'Delete Report':
            obj = get_object_or_404(Reports, id = id)
            dire = Reports.objects.filter(created_by = request.user.id)
            if obj in dire:
                obj.delete()
                messages.success(request, f'Report    "{ obj }"   has been deleted!')
                return redirect('dr_manage_reports')
            else:
                messages.warning(request, f'Report    "{ obj }"   no longer exists !')
                return redirect('dr_manage_reports')

        elif request.POST["submit"] == 'Update Report':
            print(request.method)
            form = reportDetailForm(request.POST or None,request.FILES or None, instance=obj)
            if form.is_valid():
                if form.cleaned_data["directorApproved"] == True:
                    obj.directorApprovedDate = date.today()
                form = reportDetailForm(request.POST or None,request.FILES or None, instance=obj)
                form.save()
                messages.success(request, f'Report has been Updated!')
                return HttpResponseRedirect("/director/report-detail/"+ str(id)) 
            else:
                form = reportDetailForm(request.POST or None,request.FILES or None, instance=obj)
                context["form"] = form
                return render(request, "director/report_detail.html", context)
    else:
        form = reportDetailForm(instance=obj)
        context["form"] = form

    return render(request, "director/report_detail.html", context)





@login_required
def reportsArchive(request):
    context = {}
    context["data"] = User.objects.get(username = request.user.username)
    rol = request.user.role
    context["role"] = len(str(rol))
    context["date"] = date.today()
    context["lists"] = Reports.objects.all().order_by('-dateAdded')

    return render(request, "director/reports_archive.html", context)
