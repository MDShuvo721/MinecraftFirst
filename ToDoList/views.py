from django.shortcuts import render, redirect, get_object_or_404
from .models import Task, Worlds, World_Tasks
from django.http import JsonResponse
from .utils import render_task_box
from django.contrib.auth.decorators import login_required
from .forms import NewWorld

# Create your views here.
@login_required(login_url = "SignLog:login")
def worlds(request):
    worlds = Worlds.objects.filter(user=request.user)
    form = NewWorld()  # Instantiate the form
    
    context = {
        'worlds': worlds,
        'form': form,
    }
    
    return render(request, 'ToDoList/worlds.html', context)

@login_required(login_url = "SignLog:login")
def show_task(request, world_id):
    world = get_object_or_404(Worlds, pk=world_id)
    world_tasks = World_Tasks.objects.filter(world=world, is_complete=False)
    return render(request, 'ToDoList/Tasks.html', {'world': world, 'world_tasks': world_tasks})

@login_required(login_url = "SignLog:login")
def complete_task(request, world_task_id):
    world_task = get_object_or_404(World_Tasks, pk=world_task_id)
    world = world_task.world
    task = world_task.tasks

    world.progress_point += task.task_point
    world_task.is_complete = True

    world.save()
    world_task.save()

    return redirect('WorldTasks:show_task', world_id=world.id)

@login_required(login_url = "SignLog:login")
def fail_task(request, world_task_id):
    world_task = get_object_or_404(World_Tasks, pk=world_task_id)
    world = world_task.world

    world.progress_point -= 10
    world.save()

    return redirect('WorldTasks:show_task', world_id=world.id)

@login_required(login_url="SignLog:login")
def create_world(request):
    if request.method == 'POST':
        form = NewWorld(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            user = request.user
            world = Worlds.objects.create(name=name, user=user)
            # Create world_tasks here
            tasks = Task.objects.all()
            for task in tasks:
                World_Tasks.objects.create(world=world, tasks=task)
            return redirect('WorldTasks:worlds_list')
    else:
        form = NewWorld()
    return render(request, 'ToDoList/create_world.html', {'form': form})



@login_required(login_url = "SignLog:login")
def delete_world(request, world_id):
    world = get_object_or_404(Worlds, pk=world_id)
    
    # Ensure the logged-in user owns the world before deleting
    if world.user == request.user:
        world.delete()
    
    return redirect('WorldTasks:worlds_list')
