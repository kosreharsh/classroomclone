from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.http import  Http404
from django.views import generic
from braces.views import SelectRelatedMixin
from . import models

from django.contrib.auth import get_user_model
User = get_user_model()
# Create your views here.

class PostList(SelectRelatedMixin,generic.ListView):
    model = models.Post
    select_related = ("user","group")

class  PostDetail(SelectRelatedMixin, generic.DetailView):
    model = models.Post
    select_related = ("user", "group")

    def get_queryset(self):
        queryset = super().get_queryset()
        return queryset.filter(
            user__username__iexact=self.kwargs.get("username")
        )    


class CreatePost(LoginRequiredMixin, SelectRelatedMixin, generic.CreateView):
    
    fields = ('message','group')
    model = models.Post

    
    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.user = self.request.user
        self.object.save()
        return super().form_valid(form)      



class DeletePost(LoginRequiredMixin, SelectRelatedMixin, generic.DeleteView):
    model = models.Post
    select_related = ("user", "group")
    slug = 'a'
    success_url = reverse_lazy("group:class_single",kwargs={'slug':slug})

    def get_queryset(self):
        queryset = super().get_queryset()
        return queryset.filter(user_id=self.request.user.id)

    def delete(self, *args, **kwargs):
        # messages.success(self.request, "Post Deleted")
        group = self.get_object().group
        slug = group.slug
        return super().delete(*args, **kwargs)
        

