
from django.shortcuts import render
from .models import Task

def render_task_box(user, task):
    return render(
        'ToDoList/Tasks.html',  # Change this to your HTML template path
        {'task': task, 'user': user}
    )
