# todo/models.py
from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

class TodoItem(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    created_at = models.DateTimeField(default=timezone.now)
    updated_at = models.DateTimeField(auto_now=True)
    due_date = models.DateTimeField(default=timezone.now)  # Due date for the task
    user = models.ForeignKey(User, on_delete=models.CASCADE)  # Link to user
    completed = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.title} - {self.description} on {self.due_date}"