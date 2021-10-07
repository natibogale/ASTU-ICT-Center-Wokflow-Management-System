from .models import *
from director.models import Projects, TeamProjectMessages
from django import forms
from authentication.models import User, Teams
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Submit, Row, Column



class DateInput(forms.DateInput):
    input_type = 'date'



class assignExpertForm(forms.ModelForm):
    

    # CHOICES=[('True','Yes'),
    # ('False','No')]
    # assignToExperts = forms.ChoiceField(choices=CHOICES, widget=forms.RadioSelect)


  
    class Meta:
        model = Projects
        # fields = '__all__'
        fields = ('assignToExperts',)


class sendMessagesForm(forms.ModelForm):
  
    class Meta:
        model = ExpertProjectMessages
        fields = ('message','projectMessageFile')

        widgets = {
            'deadLine': DateInput(),
        }

class teamSendMessagesForm(forms.ModelForm):  
    class Meta:
        model = TeamProjectMessages
        fields = ('message','projectMessageFile')

        widgets = {
            'deadLine': DateInput(),
        }



class leaderApproveForm(forms.ModelForm):  
    CHOICES=[('True','Yes'),
    ('False','No')]

    # Leader_Approved = forms.ChoiceField(choices=CHOICES, widget=forms.RadioSelect)
  
    class Meta:
        model = Projects
        fields = ('leaderApproved',)







class teamProjectDetailForm(forms.ModelForm):
    CHOICES=[('True','Yes'),
    ('False','No')]

    assignToExperts = forms.ChoiceField(choices=CHOICES, widget=forms.RadioSelect)

    def __init__(self, *args, **kwargs):
        super(teamProjectDetailForm, self).__init__(*args, **kwargs)
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
        exclude = ['is_seen','is_active','directorApproved','created_by','expertUnique','teamUnique','directorApprovedDate', 'leaderApprovedDate','assignedTeam','projectFile','dateAdded']

        widgets = {
            'deadLine': DateInput(),
        }

