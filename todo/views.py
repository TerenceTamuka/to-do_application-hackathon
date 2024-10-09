# todo/views.py
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import TodoItem
from .forms import TodoForm
from django.contrib import messages
from django.views.generic import CreateView
from django.urls import reverse_lazy
from django.shortcuts import render


def index(request):
    todo = TodoItem.objects.all()
    context = {
        'todo-list': todo,
        # Pass authentication status
        'is_authenticated': request.user.is_authenticated
    }
    return render(request, 'todo/index.html', context)


@login_required
def todo_list(request):
    # Fetch incomplete (pending) and completed to-do items for the logged-in user
    todos = TodoItem.objects.filter(user=request.user, completed=False)
    completed_todos = TodoItem.objects.filter(user=request.user, completed=True)

    # Pass the tasks to the template for rendering
    context = {
        'todos': todos,
        'completed_todos': completed_todos,
        'is_authenticated': request.user.is_authenticated,
    }

    return render(request, 'todo/todo_list.html', context)



@login_required
def todo_create(request):
    if request.method == 'POST':
        form = TodoForm(request.POST)
        if form.is_valid():
            todo = form.save(commit=False)
            todo.user = request.user  # Associate the To-Do with the logged-in user
            todo.save()
            messages.success(request, 'Your to-do item has been successfully created!')
            return redirect('todos', pk=request.user.pk)  # Redirect to the user's todo list page
    else:
        form = TodoForm()
    return render(request, 'todo/todo_form.html', {'form': form})

@login_required
def edit_todo(request, todo_id):
    # Get the to-do item instance by its ID and ensure it belongs to the logged-in user
    todo = get_object_or_404(TodoItem, id=todo_id, user=request.user)

    # Handle form submission
    if request.method == 'POST':
        form = TodoForm(request.POST, instance=todo)
        if form.is_valid():
            form.save()
            messages.success(request, 'Your to-do item has been successfully updated!')
            return redirect('todo_list')  # Redirect to user's todo list
    else:
        form = TodoForm(instance=todo)

    # Render the edit form template
    return render(request, 'todo/edit_my_todo_list.html', {'form': form, 'todo': todo})

@login_required
def delete_todo(request, pk):
    # Retrieve the to-do item by its primary key (pk) and ensure it belongs to the current user
    todo = get_object_or_404(TodoItem, id=pk, user=request.user)

    # Check if the request is POST (for deleting)
    if request.method == 'POST':
        todo.delete()  # Delete the to-do item
        messages.success(request, 'Your to-do item has been successfully deleted!')
        return redirect('todo_list')  # Redirect to the to-do list

    # Render a confirmation page if the request is GET
    return render(
        request,
        'todo/todo_confirm_delete.html',  # Template for delete confirmation
        {'todo': todo})



def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('home')
    else:
        form = UserCreationForm()
    return render(request, 'registration/signup.html', {'form': form})