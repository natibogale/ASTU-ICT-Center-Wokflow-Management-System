from .models import *
from django import forms
from authentication.models import User, Teams
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Submit, Row, Column



class DateInput(forms.DateInput):
    input_type = 'date'



class addProjectsForm(forms.ModelForm):
    # worksContractSigningDate = forms.DateField(widget=DatePickerInput(format='%Y-%m-%d'))
    # worksContractCommencementDate = forms.DateField(widget=DatePickerInput(format='%Y-%m-%d'))
    # worksContractCompletionDate_original = forms.DateField(widget=DatePickerInput(format='%Y-%m-%d'))
    # worksContractCompletionDate_revised = forms.DateField(widget=DatePickerInput(format='%Y-%m-%d'))
    # servicesContractSigningDate = forms.DateField(widget=DatePickerInput(format='%Y-%m-%d'))
    # servicesContractCommencementDate = forms.DateField(widget=DatePickerInput(format='%Y-%m-%d'))
    # servicesContractCompletionDate_original = forms.DateField(widget=DatePickerInput(format='%Y-%m-%d'))
    # servicesContractCompletionDate_revised=  forms.DateField(widget=DatePickerInput(format='%Y-%m-%d'))
    # expectedProjectCompletionDate = forms.DateField(widget=DatePickerInput(format='%Y-%m-%d'))
    # variationOrders_approvalDate = forms.DateField(widget=DatePickerInput(format='%Y-%m-%d'))
    # extentionOfTime_approvalDate =  forms.DateField(widget=DatePickerInput(format='%Y-%m-%d'))



    assignedTeam = forms.ChoiceField(choices = [])
    def __init__(self, *args, **kwargs):
        super(addProjectsForm, self).__init__(*args, **kwargs)
        self.fields['assignedTeam'].choices = [(  x.teamName , x.teamName  ) for x in Teams.objects.exclude(teamName  ='All')]

        # self.fields['assignedTeam'].choices = [(x) for x in User.objects.filter( username = 'n'  )]

    CHOICES=[('True','Yes'),
    ('False','No')]

    is_urgent = forms.ChoiceField(choices=CHOICES, widget=forms.RadioSelect)
  


    class Meta:
        model = Projects
        # fields = '__all__'
        exclude = ['dateAdded','is_seen','created_by']

        widgets = {
            'deadLine': DateInput(),
        }