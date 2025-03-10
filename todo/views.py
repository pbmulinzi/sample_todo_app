from django.shortcuts import render, redirect, get_object_or_404
from .models import Task
from .forms import TaskForm


# Create your views here.
def task_list(request):
    tasks = Task.objects.all().order_by('-created_date') 
    #there is a dash before the word 'created data' to enable the order be in descending order; from latest to oldest.
    context = {'tasks': tasks}
    return render(request, 'todo/task_list.html', context)

def task_create(request):
    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('task_list')
        
    else:
        form = TaskForm()
    context = {'form': form}
    return render(request, 'todo/task_form.html', context)

def task_update(request, pk):
    task = get_object_or_404(Task, pk=pk)
    if request.method == 'POST':
        form = TaskForm(request.POST, instance=task)
        if form.is_valid():
            form.save()
            return redirect('task_list')
        
    else:
        form = TaskForm(instance=task)
    context = {'form': form}
    return render(request, 'todo/task_form.html', context)

def task_delete(request, pk):
    task = get_object_or_404(Task, pk=pk)
    if request.method == 'POST':
        task.delete()
        return redirect('task_list')
    context = {'task': task}
    return render(request, 'todo/task_confirm_delete.html', context)

def task_complete(request, pk):
    task = get_object_or_404(Task, pk=pk)
    task.completed = not task.completed
    task.save()
    return redirect('task_list')