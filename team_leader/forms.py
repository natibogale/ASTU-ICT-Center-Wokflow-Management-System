from .models import *
from director.models import Projects
from django import forms
from authentication.models import User, Teams
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Submit, Row, Column



class DateInput(forms.DateInput):
    input_type = 'date'



class assignExpertForm(forms.ModelForm):
    
    # assignedExpert = forms.ChoiceField(choices = [])
    # def __init__(self, *args, **kwargs):
    #     team = kwargs.pop('team')
    #     fr = team
    #     print('aaaaaaaaaaaaaaaaaaaaaaaaaaaaaa',team)
    #     super(assignExpertForm, self).__init__(*args, **kwargs)

        # self.fields['assignedExpert'].choices = [(  x.pk , x.firstName  ) for x in User.objects.filter(team = team, role = 7)]

        # self.fields['assignedTeam'].choices = [(x) for x in User.objects.filter( username = 'n'  )]

    assignedExpert = forms.ModelChoiceField(queryset=User.objects.filter( role = 7 ))


  
    class Meta:
        model = Projects
        # fields = '__all__'
        fields = ('assignedExpert',)


class sendMessagesForm(forms.ModelForm):
  
    class Meta:
        model = ExpertProjectMessages
        fields = ('message','projectMessageFile')

        widgets = {
            'deadLine': DateInput(),
        }