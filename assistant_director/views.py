from datetime import date
from django.db.models.query_utils import Q
from django.http.response import HttpResponseRedirect
from django.shortcuts import get_object_or_404, render, redirect

from director.forms import profileDetail
from director.models import DirectorReportMessages
from .forms import *
from .models import *
from django.template.context_processors import csrf
from django.contrib import messages
from django.contrib.auth.decorators import login_required, user_passes_test
from authentication.models import Teams, User

# Create your views here.



ad_login_required = user_passes_test(
    lambda user: True if user.role == "Assistant Director" and not user.is_admin else False, login_url='/')


def only_ad(view_func):
    decorated_view_func = login_required(
        ad_login_required(view_func), login_url='/')
    return decorated_view_func



# Create your views here.
@login_required
def index(request):
    context = {}
    
    context["data"] = User.objects.get(username = request.user.username)
    rol = request.user.role
    context["role"] = len(str(rol))
    return render(request, 'assistant_director/index.html', context)





@login_required
def registrationView(request):
    context = {}
    # context["data"] = User.objects.get(id = id)
    context["data"] = User.objects.get(username = request.user.username)
    context["lists"] = User.objects.filter(is_admin = False)
    if request.POST:
        form = registrationForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password1')
            # auth = authenticate(username=username, password=password)
            # login(request,auth)
            messages.success(request, f'The Account is succesfully created user { username } now has access!')
            
            return redirect('ad_manage_accounts')
        else:
            form = registrationForm(request.POST)
            context ["form"] = form
            return render(request, 'assistant_director/register_user.html', context)


    else:
        form = registrationForm()
        context ["form"] = form
    return render(request, 'assistant_director/register_user.html', context)





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

            return redirect('ad_profile')

        else:
            context["form"] = form
            return render(request, 'assistant_director/profile.html', context)

    else:
        form = profileDetail(instance=obj)
        context["form"] = form

    return render(request, 'assistant_director/profile.html', context)




@login_required
def manageUsersView(request):
    context = {}
    # context["data"] = User.objects.get(id = id)
    context["data"] = User.objects.get(username = request.user.username)
    context["lists"] = User.objects.filter(is_admin = False)
    return render(request, 'assistant_director/manage_users.html', context)



@login_required
def manageReports(request):
    context = {}
    context["data"] = User.objects.get(username = request.user.username)
    rol = request.user.role
    context["role"] = len(str(rol))
    context["date"] = date.today()
    context["lists"] = Reports.objects.filter(is_active=True).order_by('-dateAdded')
    return render(request, "assistant_director/manage_reports.html", context)



# @login_required
# def forwardToTeamsView(request,id):
#     obj = get_object_or_404(Reports, id = id)
#     context = {}
#     context["data"] = User.objects.get(username = request.user.username)
#     rol = request.user.role
#     context["role"] = len(str(rol))
#     context["lists"] = Reports.objects.filter(is_active=True).order_by('-dateAdded')
#     if request.method == 'POST':
#         print(request.method)
#         form = assignTeamsForm(request.POST, request.FILES, instance = obj)
#         if form.is_valid():
#             project = form.save(commit=False)
#             project.expertUnique = uuid.uuid1()
#             project.currentlyOn = "Experts"
#             project.save()
#             messages.success(request, f'Report has been forwarded')
#             return redirect ('ad_manage_reports')
#         else:
#             form = assignTeamsForm(request.POST, request.FILES,  instance = obj)
#             context["form"] = form
#             return render(request, "team_leader/assign_teams.html", context)
#     else:
#         form = assignTeamsForm(instance = obj)
#         context["form"] = form

#     return render(request, "assistant_director/assign_teams.html", context)





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
    if request.method == 'POST':
        form = reportDetailForm(request.POST or None,request.FILES or None, instance=obj)
        if form.is_valid():
            if form.cleaned_data["assistantApproved"] == True:
                obj.assistantApprovedDate = date.today()
            form = reportDetailForm(request.POST or None,request.FILES or None, instance=obj)
            form.save()
            messages.success(request, f'Report has been Updated!')
            return HttpResponseRedirect("/assistant-director/report-detail/"+ str(id)) 
        else:
            form = reportDetailForm(request.POST or None,request.FILES or None, instance=obj)
            context["form"] = form
            return render(request, "assistant_director/report_detail.html", context)
    else:
        form = reportDetailForm(instance=obj)
        context["form"] = form

    return render(request, "assistant_director/report_detail.html", context)









@login_required
def reportMessagesView(request,id, messageTo):
    obj = get_object_or_404(Reports, id = id)
    context = {}    
    context["data"] = User.objects.get(username = request.user.username)
    rol = request.user.role
    context["obj"] = obj
    context["role"] = len(str(rol))
    acv = Teams.objects.get(id = messageTo)
    context["lists"] =  AssistantMessages.objects.filter(Q(reportId = id), Q(messageTo = messageTo) | Q(messageSender = messageTo)).order_by('sentDate')
    if request.method == 'POST':
        if request.POST["submit"] == 'Approve Report':
            form2 = assistantReportApproveForm(request.POST, instance=obj)
            if form2.is_valid():
                obj.assistantApprovedDate = date.today()
                obj.assistantApproved = True
                # if obj.deadLine < date.today():
                #     obj.is_late = True
                form2 = assistantReportApproveForm(request.POST, instance=obj)
                form2.save() 
                messages.success(request, f'Report is approved from Team Leader')
                return HttpResponseRedirect("/assistant-director/report-messages/"+ str(obj.id)+ "/"+messageTo  ) 
            else:
                form = reportSendMessagesForm()
                context["form"] = form
                form2 = assistantReportApproveForm()
                context["form2"] = form2
                return render(request, "assistant_director/report_messages.html", context)
        elif  request.POST["submit"] == 'Send Message':
            print(request.method)
            form = reportSendMessagesForm(request.POST, request.FILES)
            if form.is_valid():
                message = form.save(commit=False)
                message.messageSender = request.user
                team = Teams.objects.get(id=messageTo)
                message.messageTo = team
                message.reportId = obj
                message.save()
                messages.success(request, f'Message is sent')
                form = reportSendMessagesForm()
                context["form"] = form
                return HttpResponseRedirect("/assistant-director/report-messages/"+ str(message.reportId.id) + "/"+ messageTo) 
            else:
                form = reportSendMessagesForm(request.POST, request.FILES)
                context["form"] = form
                form2 = assistantReportApproveForm()
                context["form2"] = form2
                return render(request, "assistant_director/report_messages.html", context)
    else:
        form = reportSendMessagesForm()
        context["form"] = form
        form2 = assistantReportApproveForm()
        context["form2"] = form2

    return render(request, "assistant_director/report_messages.html",context)




@login_required
def reportsArchive(request):
    context = {}
    context["data"] = User.objects.get(username = request.user.username)
    rol = request.user.role
    context["role"] = len(str(rol))
    context["date"] = date.today()
    context["lists"] = Reports.objects.all().order_by('-dateAdded')
    return render(request, "assistant_director/reports_archive.html", context)







@login_required
def directorReportMessagesView(request,id):
    obj = get_object_or_404(Reports, id = id)
    context = {}    
    context["data"] = User.objects.get(username = request.user.username)
    rol = request.user.role
    context["obj"] = obj
    context["role"] = len(str(rol))
    context["lists"] =  DirectorReportMessages.objects.filter( reportId = id).order_by('sentDate')
    if request.method == 'POST':
        print(request.method)
        form = directorReportSendMessagesForm(request.POST, request.FILES)
        if form.is_valid():
            message = form.save(commit=False)
            message.messageSender = request.user
            to = User.objects.get(role=1)
            message.messageTo = to
            message.reportId = obj
            message.save()
            messages.success(request, f'Message is sent')
            form = directorReportSendMessagesForm()
            context["form"] = form
            return HttpResponseRedirect("/assistant-director/director-report-messages/"+ str(message.reportId.id) ) 
        else:
            form = directorReportSendMessagesForm(request.POST, request.FILES)
            context["form"] = form
   
            return render(request, "assistant_director/director_report_messages.html", context)
    else:
        form = directorReportSendMessagesForm()
        context["form"] = form

    return render(request, "assistant_director/director_report_messages.html",context)


