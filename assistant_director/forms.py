
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.core.validators import validate_slug, validate_email
from assistant_director.models import AssistantMessages
from authentication.models import User
from director.models import DirectorReportMessages, Reports






gender = (
        ('Male','Male'),
        ('Female','Female'),
        )

class DateInput(forms.DateInput):
    input_type = 'date'

class registrationForm(UserCreationForm):
    email = forms.EmailField(max_length=500, help_text="Required. Add a valid email address")
    firstName = forms.CharField(max_length=500, required=True,widget= forms.TextInput (attrs={'class':'form-control col-md-auto','id':'exampleInputUsername1'}))
    lastName = forms.CharField(max_length=500, required=True,widget= forms.TextInput (attrs={'class':'form-control col-md-auto','id':'exampleInputUsername1'}))

    # middleName = forms.CharField(max_length=500, required=True)
    # title = forms.ChoiceField(choices=titles, required=True)

    class Meta:
        model = User
        fields = ("username", "firstName","lastName","gender",
                  "email","role","team", "password1", "password2")

    # def form_valid(self, form):
    #     form.instance.registeredBy = self.request.user
    #     return super().form_valid(form)

    def __init__(self, *args, **kwargs):
        super(registrationForm, self).__init__(*args, **kwargs)
        self.fields['team'].required = True


    def clean_username(self):
        passed = self.cleaned_data['username']
        print ("#####################################",passed)
        if not passed:
            raise forms.ValidationError("A user with this username exists. Make sure it is unique!")
        return passed

    # def clean(self):
    #     directorate= self.cleaned_data['directorate']
    #     team = self.cleaned_data['team']
    #     print ("#####################################",title)
    #     if title=='Director':
    #         for instance in User.objects.all():
    #             if instance.title == title and instance.directorate == directorate and instance.is_active:
    #                 raise forms.ValidationError("There is a Director registered for this Directorate! There can only be one director. You first must remove the previous director to continue!")
    #     if title=='Team Leader':
    #         for instance in User.objects.all():
    #             if instance.title == title and instance.team == team and instance.is_active:
    #                 raise forms.ValidationError("There is a Team Leader registered for this Team! There can only be one Team Leader. You first must remove the previous Team Leader to continue!")




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
        'leaderApproved','directorApprovedDate',
        'assistantApprovedDate','leaderApprovedDate','reportFile','is_active']

        widgets = {
            'deadLine': DateInput(),
        }




class assistantReportApproveForm(forms.ModelForm):  
    CHOICES=[('True','Yes'),
    ('False','No')]

    # Leader_Approved = forms.ChoiceField(choices=CHOICES, widget=forms.RadioSelect)
  
    class Meta:
        model = Reports
        fields = ('assistantApproved',)


class reportSendMessagesForm(forms.ModelForm):
  
    class Meta:
        model = AssistantMessages
        fields = ('message','reportMessageFile')

        widgets = {
            'deadLine': DateInput(),
        }






class directorReportSendMessagesForm(forms.ModelForm):
  
    class Meta:
        model = DirectorReportMessages
        fields = ('message','reportMessageFile')

        widgets = {
            'deadLine': DateInput(),
        }