from django.shortcuts import render, redirect, HttpResponse
from django.urls import reverse, reverse_lazy
from .models import Assignment, Response
from django.contrib import messages
from django.core.exceptions import ObjectDoesNotExist
from .forms import AssignmentForm, ResponseForm, AssignmentFilesForm
from group.models import Group
# Create your views here.


def delete(request, pk):
    try:
        assignment = Assignment.objects.get(pk=pk)
        group_slug = assignment.group.slug
        assignment.delete()
        return reverse_lazy('group:class_single', kwargs={'slug': group_slug})
    except ObjectDoesNotExist:
        messages.warning(request, "Assignment is not found")
        return redirect('group:base1')


def update_assignment(request, pk):
    context = {}
    assignment = Assignment.objects.get(pk=pk)
    group_slug = assignment.group.slug
    form = AssignmentForm(request.POST or None, instance=assignment)
    if form.is_valid():
        form.save()
        return reverse('group:class_single', kwargs={'slug': group_slug})
    context['assignment_form'] = form
    return render(request, "update-assignment.html", context)


def create_assignment(request, slug):
    context = {}
    group = Group.objects.filter(slug=slug)[0]
    if request.method == 'POST':
        form = AssignmentForm(request.POST)
        filesform = AssignmentFilesForm(request.POST, request.FILES)
        if form.is_valid():
            form.instance.group = group
            form.save()
            return reverse('group:class_single', kwargs={'slug': group.slug})
    context['assignment_form'] = AssignmentForm()
    context['filesform'] = AssignmentFilesForm()
    return render(request, "create-assignment.html", context)


def assignment_detail(request, slug):
    assignment = Assignment.objects.filter(slug=slug)[0]
    form = ResponseForm(request.POST or None)
    if form.is_valid():
        form.save()
        messages.success(request, "Assignment has been Successfully Added")
        return render(request, "assignment_detail.html", {})

    context = {
        'object': assignment,
        'form': form,
    }

    return render(request, 'assignment-detail.html', context)
