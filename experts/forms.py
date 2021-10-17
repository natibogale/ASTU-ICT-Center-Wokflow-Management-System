from django.forms.widgets import DateInput
from .models import *
from director.models import Projects, Reports
from django import forms
from authentication.models import User, Teams
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Submit, Row, Column






class expertProjectDetailForm(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        super(expertProjectDetailForm, self).__init__(*args, **kwargs)
        self.fields['projectDescription'].widget.attrs['readonly'] = True 
        self.fields['projectTitle'].widget.attrs['readonly'] = True 

        # self.fields['assignedTeam'].choices = [(x) for x in User.objects.filter( username = 'n'  )]

    CHOICES=[('True','Yes'),
    ('False','No')]
    # projectDescription = forms.CharField(widget=forms.TextInput(attrs={'readonly':'readonly'}))
    # projectFile = forms.FileField(widget=forms.TextInput(attrs={'readonly':'readonly'}))

    deadLine = forms.CharField(widget=forms.TextInput(attrs={'readonly':'readonly'}))
    is_urgent = forms.CharField(widget=forms.TextInput(attrs={'readonly':'readonly'}))
    is_late = forms.CharField(widget=forms.TextInput(attrs={'readonly':'readonly'}))

    currentlyOn = forms.CharField(widget=forms.TextInput(attrs={'readonly':'readonly'}))

    class Meta:
        model = Projects
        # fields = '__all__'
        exclude = ['is_seen','is_active','directorApproved','created_by','expertUnique','teamUnique','directorApprovedDate', 'leaderApprovedDate','assignedTeam','projectFile','dateAdded','leaderApproved', 'assignToExperts']

        widgets = {
            'deadLine': DateInput(),
        }






class reportDetailForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(reportDetailForm, self).__init__(*args, **kwargs)
        self.fields['reportTitle'].widget.attrs['readonly'] = True 
        self.fields['reportsDescription'].widget.attrs['readonly'] = True 
        self.fields['deadLine'].widget.attrs['readonly'] = True 
        self.fields['dateAdded'].widget.attrs['readonly'] = True 
        self.fields['is_late'].widget.attrs['readonly'] = True 

    dateAdded = forms.CharField(
    widget=forms.TextInput(attrs={'readonly':'readonly'}))
    class Meta:
        model = Reports
        # fields = '__all__'
        exclude = ['created_by','is_seen','directorUnique','directorApproved',
        'directorApprovedDate','assistantApproved',
        'assistantApprovedDate','reportFile','is_active']

        widgets = {
            'deadLine': DateInput(),
        }   