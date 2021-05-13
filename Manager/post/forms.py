from django import forms

from post import models


class PostForm(forms.ModelForm):
    message = forms.CharField(widget=forms.TextInput(attrs={
        'class' : 'form-control', 
        'row' : '2'
    }))
    class Meta:
        fields = ['message']
        model = models.Post

    # def __init__(self, *args, **kwargs):
    #     user = kwargs.pop("user", None)
    #     super().__init__(*args, **kwargs)
    #     if user is not None:
    #         self.fields["group"].queryset = (
    #             models.Group.objects.filter(
    #                 pk__in=user.groups.values_list("group__pk")
    #             )
    #         )
