from django.contrib import admin
from .models import TodoItem
from django_summernote.admin import SummernoteModelAdmin

# Register your models here.

class TodoAdmin(SummernoteModelAdmin):
    summernote_fields = (
        'title',
        'description',  # Use Summernote for description and additional
    )
    list_filter = [
        'created_at',
        'updated_at',  
    ]



# Register your models here.
admin.site.register(TodoItem, TodoAdmin)
