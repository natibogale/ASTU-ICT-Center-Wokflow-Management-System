from .models import *
from django import forms
from authentication.models import User, Teams
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Submit, Row, Column



class DateInput(forms.DateInput):
    input_type = 'date'



class addProjectsForm(forms.ModelForm):

    assignedTeam = forms.ModelChoiceField(queryset=Teams.objects.exclude(teamName  ='All'))
    # def __init__(self, *args, **kwargs):
    #     super(addProjectsForm, self).__init__(*args, **kwargs)
    #     self.fields['assignedTeam'].choices = [(  x , x.teamName  ) for x in Teams.objects.exclude(teamName  ='All')]

        # self.fields['assignedTeam'].choices = [(x) for x in User.objects.filter( username = 'n'  )]

    CHOICES=[('True','Yes'),
    ('False','No')]

    is_urgent = forms.ChoiceField(choices=CHOICES, widget=forms.RadioSelect)
  
    class Meta:
        model = Projects
        # fields = '__all__'
        exclude = ['dateAdded','is_seen','created_by','is_active','assignToExperts','currentlyOn','expertUnique','teamUnique','directorApproved','leaderApproved','directorApprovedDate', 'leaderApprovedDate', 'is_late']

        widgets = {
            'deadLine': DateInput(),
        }



class sendMessagesForm(forms.ModelForm):
  
    class Meta:
        model = TeamProjectMessages
        fields = ('message','projectMessageFile')

        widgets = {
            'deadLine': DateInput(),
        }


class directorApproveForm(forms.ModelForm):  
    CHOICES=[('True','Yes'),
    ('False','No')]

    # Leader_Approved = forms.ChoiceField(choices=CHOICES, widget=forms.RadioSelect)
  
    class Meta:
        model = Projects
        fields = ('directorApproved',)



class projectDetailForm(forms.ModelForm):

    assignedTeam = forms.ModelChoiceField(queryset=Teams.objects.exclude(teamName  ='All'))
    # def __init__(self, *args, **kwargs):
    #     super(addProjectsForm, self).__init__(*args, **kwargs)
    #     self.fields['assignedTeam'].choices = [(  x , x.teamName  ) for x in Teams.objects.exclude(teamName  ='All')]

        # self.fields['assignedTeam'].choices = [(x) for x in User.objects.filter( username = 'n'  )]

    CHOICES=[('True','Yes'),
    ('False','No')]

    is_urgent = forms.ChoiceField(choices=CHOICES, widget=forms.RadioSelect)
    dateAdded = forms.CharField(
    widget=forms.TextInput(attrs={'readonly':'readonly'}))
    currentlyOn = forms.CharField(widget=forms.TextInput(attrs={'readonly':'readonly'}))

    class Meta:
        model = Projects
        # fields = '__all__'
        exclude = ['is_seen','created_by','expertUnique','teamUnique', 'leaderApprovedDate','assignToExperts','leaderApproved','directorApprovedDate']

        widgets = {
            'deadLine': DateInput(),
        }




class profileDetail(forms.ModelForm):

    class Meta:
        model = User
        exclude = ['password','is_admin','role','team','is_active','is_staff', 'is_superuser', 'date_joined','last_login', 'last_edit']

        widgets = {
            'deadLine': DateInput(),
        }








class requestReportsForm(forms.ModelForm):

    class Meta:
        model = Reports
        # fields = '__all__'
        exclude = ['dateAdded','is_seen','created_by','is_active',
        'currentlyOn','expertUnique','teamUnique',
        'directorApproved','leaderApproved','directorApprovedDate', 
        'directorUnique','assistantApprovedDate','assistantApproved',
        'leaderApprovedDate', 'is_late']

        widgets = {
            'deadLine': DateInput(),
        }



class reportSendMessagesForm(forms.ModelForm):
  
    class Meta:
        model = DirectorReportMessages
        fields = ('message','reportMessageFile')

        widgets = {
            'deadLine': DateInput(),
        }



class directorReportApproveForm(forms.ModelForm):  
    CHOICES=[('True','Yes'),
    ('False','No')]

    # Leader_Approved = forms.ChoiceField(choices=CHOICES, widget=forms.RadioSelect)
  
    class Meta:
        model = Reports
        fields = ('directorApproved',)





class reportDetailForm(forms.ModelForm):


    dateAdded = forms.CharField(
    widget=forms.TextInput(attrs={'readonly':'readonly'}))

    class Meta:
        model = Reports
        # fields = '__all__'
        exclude = ['created_by','is_seen','directorUnique',
        'leaderApproved', 'assistantApproved','directorApprovedDate',
        'assistantApprovedDate','leaderApprovedDate']

        widgets = {
            'deadLine': DateInput(),
        }