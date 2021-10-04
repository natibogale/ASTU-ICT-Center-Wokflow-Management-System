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
        exclude = ['dateAdded','is_seen','created_by','is_active','assignedExpert','currentlyOn','expertUnique','teamUnique']

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

