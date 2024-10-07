# todo/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('', views.todo_list, name='todo-list'),
    path('create/', views.todo_create, name='todo-create'),
    path('edit/<int:pk>/', views.todo_edit, name='todo-edit'),
    path('delete/<int:pk>/', views.todo_delete, name='todo-delete'),
]