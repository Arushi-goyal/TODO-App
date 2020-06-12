from .models import *
from django.shortcuts import render, redirect
from django.http import HttpResponse

from .forms import workplaceform, taskform


# Create your views here.
def index(request):
    works = Addworkplace.objects.all()
    form = workplaceform()
    if request.method == "POST":
        form = workplaceform(request.POST)
        if form.is_valid():
            form.save()
        return redirect('/')
    context = {'works': works, 'form': form}
    return render(request, "workspace/list.html", context)


def index2(request):
    tasks = Addtask.objects.all()
    form = taskform()
    if request.method == "POST":
        form = taskform(request.POST)
        if form.is_valid():
            form.save()
        return redirect('/')
    context = {'tasks': tasks, 'form': form}
    return render(request, "workspace/list.html", context)


