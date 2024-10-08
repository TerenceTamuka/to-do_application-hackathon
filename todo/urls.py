from django.urls import path
from . import views

urlpatterns = [
    # Home page that displays the list of to-do items (index)
    path('', views.index, name='index'),

    path('todo/<int:pk>/', views.todo_list, name='todos'),

    # View for adding a new to-do item
    path('todo/new/', views.todo_create, name='todo_form'),

    # View for editing an existing to-do item
    path('todo/<int:pk>/edit/', views.edit_todo, name='edit_todo'),

    # View for deleting a specific to-do item
    path('todo/<int:pk>/delete/', views.delete_todo, name='todo_confirm_delete'),

    path('register/', views.register, name='register'),
]

