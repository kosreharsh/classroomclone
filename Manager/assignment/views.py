from django.shortcuts import render, redirect , HttpResponse
from django.urls import reverse, reverse_lazy
from .models import Assignment, Response
from django.contrib import messages
from django.core.exceptions import ObjectDoesNotExist
from .forms import AssignmentForm
# Create your views here.

def delete(request,pk):
    try:
        assignment = Assignment.objects.get(pk=pk)
        group_slug = asssignment.group.slug
        assignment.delete()
        return reverse_lazy('group:class_single',kwargs={'slug':group_slug })
    except ObjectDoesNotExist:
        messages.warning(request,"Assignment is not found")
        return redirect('group:base1')

def update_assignment(request, assignment):
    context = {}
    assignment = Assignment.objects.get(pk=pk)
    group_slug = asssignment.group.slug
    form = AssignmentForm(request.POST or None , instance=assignment)
    if form.is_valid():
        form.save()
        return reverse('group:class_single',kwargs={'slug':group_slug })
    context['assignment_form'] = form 
    return render(request,"update_view.html",context)

def create_assignment(request,slug):
    context = {}
    group = Group.objects.get(slug=slug)
    form = AssignmentForm(request.POST or None)
    if form.is_valid():
        form.instance.group = group
        form.save()
        return reverse('group:class_single',kwargs={'slug':slug })
    context['assignment_form'] = form 
    return render(request,"create_view.html",context)

def assignment_detail(request,slug):
    assignment = Asssignment.objects.filter(slug=slug)[0]
    form = ResponseForm(request.POST or None)
    if form.is_valid():
        form.save()
        
    context = {
        'object': assignment,
        'form': form,
    }

    return render(request,'detail-view.html',context)



