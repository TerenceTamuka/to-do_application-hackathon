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
    todo = todo.objects.all()
    context = {
        'todo-list': todo,
        # Pass authentication status
        'is_authenticated': request.user.is_authenticated
    }
    return render(request, 'tod/index.html', context)

def service_detail(request, pk):
    # function code
    TodoItem = get_object_or_404(TodoItem, pk=pk)
    return render(
        request,
        'todo/todo_list.html',
        {'todo': TodoItem})

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
            messages.success(request, 'Your to-do item has been successfully created!')
            return redirect('todo-list')
    else:
        form = TodoForm()
    return render(request, 'todo/todo_form.html', {'form': form})


@login_required
def edit_todo(request, todo_id):
    # Get the to-do item instance by its ID and ensure it belongs to the logged-in user
    todo = get_object_or_404(ToDo, id=todo_id, user=request.user)

    # Ensure the to-do item belongs to the logged-in user
    if todo.user != request.user:
        return redirect('todo_list')  # Redirect to the to-do list if unauthorized

    # Handle form submission
    if request.method == 'POST':
        form = ToDoForm(request.POST, instance=todo)  # Update the to-do item with new data
        if form.is_valid():
            form.save()  # Save changes
            messages.success(request, 'Your to-do item has been successfully updated!')
            return redirect('todo_list')  # Redirect back to the to-do list

    else:
        form = ToDoForm(instance=todo)  # Pre-fill the form with the existing to-do item details

    # Render the edit form template
    return render(
        request,
        'todo_app/edit_my_todo_list.html',  # Your template for editing to-do items
        {'form': form, 'todo': todo}
    )

@login_required
def delete_todo(request, pk):
    # Retrieve the to-do item by its primary key (pk) and ensure it belongs to the current user
    todo = get_object_or_404(ToDo, pk=pk, user=request.user)

    # Check if the request is POST (for deleting)
    if request.method == 'POST':
        todo.delete()  # Delete the to-do item
        messages.success(request, 'Your to-do item has been successfully deleted!')
        return redirect('todo_list')  # Redirect to the to-do list

    # Render a confirmation page if the request is GET
    return render(
        request,
        'todo_app/todo_confirm_delete.html',  # Template for delete confirmation
        {'todo': todo}
    )

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