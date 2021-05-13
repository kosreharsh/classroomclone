from django import forms
from .models import Assignment,Response

class AssignmentForm(forms.ModelForm):
    class Meta:
        fields = ('task','attachments','deadline')
        model = Assignment

class ResponseForm(forms.ModelForm):
    class Meta:
        fields = ('responses')