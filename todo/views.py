# todo/views.py
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import TodoItem
from .forms import TodoForm

@login_required
def todo_list(request):
    todos = TodoItem.objects.filter(user=request.user)
    return render(request, 'todo/todo_list.html', {'todos': todos})

@login_required
def todo_create(request):
    if request.method == 'POST':
        form = TodoForm(request.POST)
        if form.is_valid():
            todo = form.save(commit=False)
            todo.user = request.user  # Associate the To-Do with the logged-in user
            todo.save()
            return redirect('todo-list')
    else:
        form = TodoForm()
    return render(request, 'todo/todo_form.html', {'form': form})

@login_required
def todo_edit(request, pk):
    todo = get_object_or_404(TodoItem, pk=pk, user=request.user)
    if request.method == 'POST':
        form = TodoForm(request.POST, instance=todo)
        if form.is_valid():
            form.save()
            return redirect('todo-list')
    else:
        form = TodoForm(instance=todo)
    return render(request, 'todo/todo_form.html', {'form': form})

@login_required
def todo_delete(request, pk):
    todo = get_object_or_404(TodoItem, pk=pk, user=request.user)
    if request.method == 'POST':
        todo.delete()
        return redirect('todo-list')
    return render(request, 'todo/todo_confirm_delete.html', {'todo': todo})
