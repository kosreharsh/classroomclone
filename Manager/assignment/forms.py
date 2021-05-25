from django import forms
from .models import Assignment, ResponseFiles, AssignmentFiles


class AssignmentForm(forms.ModelForm):
    class Meta:
        model = Assignment
        fields = ('title', 'task', 'deadline')


class AssignmentFilesForm(forms.ModelForm):
    class Meta:
        model = AssignmentFiles
        fields = ('attachments',)


class ResponseForm(forms.ModelForm):
    class Meta:
        model = ResponseFiles
        fields = ('rfiles',)
