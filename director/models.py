from django.db import models
from django.conf import settings
from django.db.models.base import Model
from django.db.models.fields import UUIDField
from django.utils import timezone
import uuid
from django.core.exceptions import ValidationError




def validate_file(value):
    filesize= value.size
    if filesize > 10485760:
        raise ValidationError("The maximum file size that can be uploaded is 10MB")
    import os
    ext = os.path.splitext(value.name)[1]
    if settings.DEBUG:
        if not ext in settings.LETTER_EXT:
            raise ValidationError(u'File type not supported! Please upload only: .pdf, .doc, .docx, .rtf, .zip, .rar, .jpg, .jpeg, .png, .txt files.')


class Projects(models.Model):
    id = models.AutoField(primary_key=True)
    projectTitle = models.CharField(max_length=50, verbose_name="Project Title")
    projectDescription = models.TextField(verbose_name="Project Description")
    deadLine = models.DateField(verbose_name="Project DeadLine")
    created_by = models.ForeignKey('authentication.User' , on_delete=models.CASCADE , max_length=200, verbose_name="Project Created By")
    is_seen = models.BooleanField(default=False)
    is_urgent = models.BooleanField(default=False, verbose_name="Is Urgent")
    dateAdded = models.DateTimeField(default=timezone.now,verbose_name="Date Added")
    assignedTeam = models.ForeignKey('authentication.Teams', on_delete=models.CASCADE, max_length=300, verbose_name="Assign Project to")
    assignedExpert = models.ForeignKey('authentication.User', on_delete=models.CASCADE, related_name="+", blank=True, null=True, verbose_name="Assigned Expert")
    projectFile = models.FileField(upload_to='project_documents/',verbose_name="Project File", blank=True, validators=[validate_file])
    teamUnique = models.UUIDField(default=uuid.uuid1)
    expertUnique = models.UUIDField(blank=True, null=True,unique=True)
    currentlyOn = models.CharField(max_length=500, blank=True, null=True)
    is_active = models.BooleanField(default=True)


    
    def __str__(self):
        return f'{self.projectTitle}'

    class Meta:
        verbose_name_plural = 'Projects'



# class TeamProjects(models.Model):
#     id = models.AutoField(primary_key=True)
#     projectId = models.ForeignKey(Projects ,on_delete=models.CASCADE, max_length=500, verbose_name="Project ID")
#     forwardedTo = models.ForeignKey('authentication.User' , on_delete=models.CASCADE , max_length=200, verbose_name="Project Forwarded To")
#     is_seen = models.BooleanField(default=False)

#     def __str__(self):
#         return f'{self.projectTitle}'
#     class Meta:
#         verbose_name_plural = 'Projects'


class TeamProjectMessages(models.Model):
    id = models.AutoField(primary_key=True)
    projectId = models.ForeignKey(Projects ,on_delete=models.CASCADE, max_length=500, verbose_name="Project ID")
    projectUnique = models.CharField(max_length=500, blank=True, null=True)
    messageSender = models.ForeignKey('authentication.User' ,related_name="+", on_delete=models.CASCADE , max_length=200, verbose_name="Message From")
    messageTo = models.ForeignKey('authentication.User' , on_delete=models.CASCADE , max_length=200, verbose_name="Message To")    
    message = models.TextField(verbose_name="Message")
    projectMessageFile = models.FileField(upload_to='message_documents/',verbose_name="Message File", blank=True, validators=[validate_file])
    sentDate = models.DateTimeField(default=timezone.now,verbose_name="Date Sent")
    isFirstMessage = models.BooleanField(default=False)
    is_seen = models.BooleanField(default=False)


    def __str__(self):
        return f'{self.id}'
    class Meta:
        verbose_name_plural = 'Team Project Messages'




# class ProjectFiles(models.Model):
#     id = models.AutoField(primary_key=True)
#     projectId = models.ForeignKey(Projects ,on_delete=models.CASCADE, max_length=500, verbose_name="Project ID")
#     messageSender = models.ForeignKey('authentication.User' ,related_name="+", on_delete=models.CASCADE , max_length=200, verbose_name="Message From")
#     messageTo = models.ForeignKey('authentication.User' , on_delete=models.CASCADE , max_length=200, verbose_name="File To")    
#     projectFile = models.FileField(upload_to='project_documents/',verbose_name="Project File", blank=True, validators=[validate_file])
#     is_seen = models.BooleanField(default=False)

#     def __str__(self):
#         return f'{self.projectTitle}'
#     class Meta:
#         verbose_name_plural = 'Projects'


