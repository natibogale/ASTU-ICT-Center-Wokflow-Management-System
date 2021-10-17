from django.conf import settings
from django.db import models
from django.utils import timezone
import uuid
from django.core.exceptions import ValidationError

from director.models import Reports




def validate_file(value):
    filesize= value.size
    if filesize > 10485760:
        raise ValidationError("The maximum file size that can be uploaded is 10MB")
    import os
    ext = os.path.splitext(value.name)[1]
    if settings.DEBUG:
        if not ext in settings.LETTER_EXT:
            raise ValidationError(u'File type not supported! Please upload only: .pdf, .doc, .docx, .rtf, .zip, .rar, .jpg, .jpeg, .png, .txt files.')



# class TeamReportMessages(models.Model):
#     id = models.AutoField(primary_key=True)
#     reportId = models.ForeignKey(Reports ,on_delete=models.CASCADE, max_length=500, verbose_name="Report ID")
#     messageSender = models.ForeignKey('authentication.User' ,related_name="+", on_delete=models.CASCADE ,blank=True,null=True, max_length=200, verbose_name="Message From")
#     messageTo = models.ForeignKey('authentication.User' , on_delete=models.CASCADE , max_length=200, verbose_name="Message To")    
#     message = models.TextField(verbose_name="Message",blank=True,null=True)
#     reportMessageFile = models.FileField(upload_to='message_documents/',verbose_name="Message File", blank=True, validators=[validate_file])
#     sentDate = models.DateTimeField(default=timezone.now,verbose_name="Date Sent")
#     isFirstMessage = models.BooleanField(default=False)
#     is_seen = models.BooleanField(default=False)


#     def __str__(self):
#         return f'{self.id}'
#     class Meta:
#         verbose_name_plural = 'Team Report Messages'




class AssistantMessages(models.Model):
    id = models.AutoField(primary_key=True)
    reportId = models.ForeignKey(Reports ,on_delete=models.CASCADE, max_length=500, verbose_name="Report ID")
    messageSender = models.ForeignKey('authentication.User' ,related_name="+", on_delete=models.CASCADE ,blank=True,null=True, max_length=200, verbose_name="Message From")
    messageTo = models.ForeignKey('authentication.Teams' ,to_field='id', on_delete=models.CASCADE , max_length=200, verbose_name="Message To")    
    message = models.TextField(verbose_name="Message",blank=True,null=True)
    reportMessageFile = models.FileField(upload_to='message_documents/',verbose_name="Message File", blank=True, validators=[validate_file])
    sentDate = models.DateTimeField(default=timezone.now,verbose_name="Date Sent")
    isFirstMessage = models.BooleanField(default=False)
    is_seen = models.BooleanField(default=False)


    def __str__(self):
        return f'{self.id}'
    class Meta:
        verbose_name_plural = 'Assistant Director Report Messages'


# class ApproveReportTeam(models.Model):
#     id = models.AutoField(primary_key=True)
#     team = models.ForeignKey('authentication.Teams' ,to_field='id', on_delete=models.CASCADE , blank=True, null=True,max_length=200, verbose_name="Team")    
#     assistantApproved = models.BooleanField(default=False, blank=True, null=True, verbose_name="Approve report from Team")
#     assistantApprovedDate = models.DateField(auto_now=False, auto_now_add=False, default =None, blank=True, null=True, verbose_name="Approve Report from  Team")


#     def __str__(self):
#         return f'{self.id}'
#     class Meta:
#         verbose_name_plural = 'Approve reports from teams'