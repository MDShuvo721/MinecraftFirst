from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import Task, Worlds, World_Tasks
from SignLog.models import CustomUser

@receiver(post_save, sender=Task)
def add_task_to_worlds(sender, instance, created, **kwargs):
    if created:
        print("Signal triggered")
        worlds = Worlds.objects.all()
        for world in worlds:
            print(f"Creating World_Tasks entry for world {world.name}")
            World_Tasks.objects.create(world=world, tasks=instance)
